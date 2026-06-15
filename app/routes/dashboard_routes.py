from datetime import datetime

from flask import Blueprint, redirect, render_template, request, url_for
from pymongo.errors import PyMongoError

from app.models import ClassModel, EnrollmentModel, PaymentModel, ServiceModel, UserModel
from app.repositories import (
    ClassRepository,
    EnrollmentRepository,
    PaymentRepository,
    ProfessionalRepository,
    ServiceRepository,
    StudentRepository,
    UserRepository,
)


dashboard_bp = Blueprint("dashboard", __name__)

service_repository = ServiceRepository()
class_repository = ClassRepository()
payment_repository = PaymentRepository()
user_repository = UserRepository()
enrollment_repository = EnrollmentRepository()
student_repository = StudentRepository()
professional_repository = ProfessionalRepository()


@dashboard_bp.get("/dashboard")
def dashboard():
    role = request.args.get("role", "admin")
    user_id = request.args.get("user_id")

    db_error = None

    try:
        services = service_repository.find_all()
        classes = _classes_with_service_names(class_repository.find_all(), services)
        students = student_repository.find_all()
        professionals = professional_repository.find_all()
        payments = payment_repository.find_all()
        users = user_repository.find_all()
        payments = _payments_with_names(payments, services, students)
        enrollments = _enrollments_with_names(
            enrollment_repository.find_all(),
            services,
            classes,
            students,
        )
    except PyMongoError as error:
        from seed import build_dashboard_preview_data

        preview_data = build_dashboard_preview_data()
        services = preview_data["services"]
        classes = _classes_with_service_names(preview_data["classes"], services)
        students = preview_data["students"]
        professionals = preview_data["professionals"]
        payments = _payments_with_names(preview_data["payments"], services, students)
        users = preview_data["users"]
        enrollments = _enrollments_with_names(
            preview_data["enrollments"],
            services,
            classes,
            students,
        )
        db_error = str(error)

    financial_summary = _financial_summary(payments)

    return render_template(
        "dashboard.html",
        role=role,
        user_id=user_id,
        services=services,
        classes=classes,
        payments=payments,
        users=users,
        students=students,
        professionals=professionals,
        enrollments=enrollments,
        financial_summary=financial_summary,
        db_error=db_error,
    )


@dashboard_bp.post("/dashboard/admin/users")
def create_user_from_dashboard():
    user = UserModel(
        name=request.form["name"],
        email=request.form["email"],
        role=request.form["role"],
        password=request.form["password"],
        related_id=request.form.get("related_id") or None,
    )
    user_repository.insert_user(user)
    return redirect(url_for("dashboard.dashboard", role="admin"))


@dashboard_bp.post("/dashboard/admin/users/<user_id>/role")
def update_user_role_from_dashboard(user_id):
    user_repository.update_role(user_id, request.form["role"])
    return redirect(url_for("dashboard.dashboard", role="admin"))


@dashboard_bp.post("/dashboard/professor/services")
def create_professor_service():
    service = ServiceModel(
        name=request.form["name"],
        category=request.form["category"],
        service_type=request.form.get("service_type", "aula"),
        monthly_price=_optional_float(request.form.get("monthly_price")),
        is_free=request.form.get("is_free") == "on",
        notes=request.form.get("notes") or None,
    )
    service_id = service_repository.insert_service(service)

    if request.form.get("day_of_week") or request.form.get("schedule_notes"):
        class_repository.insert_class(
            ClassModel(
                service_id=service_id,
                day_of_week=request.form.get("day_of_week") or None,
                start_time=request.form.get("start_time") or None,
                end_time=request.form.get("end_time") or None,
                professional_id=request.form.get("professional_id") or None,
                schedule_notes=request.form.get("schedule_notes") or None,
            )
        )

    return redirect(url_for("dashboard.dashboard", role="professor"))


@dashboard_bp.post("/dashboard/aluno/enrollments")
def enroll_student():
    class_model = class_repository.find_by_id(request.form["class_id"])
    if not class_model:
        return redirect(url_for("dashboard.dashboard", role="aluno"))

    enrollment = EnrollmentModel(
        student_id=request.form["student_id"],
        class_id=request.form["class_id"],
        service_id=class_model["service_id"],
    )
    enrollment_repository.insert_enrollment(enrollment)
    return redirect(url_for("dashboard.dashboard", role="aluno"))


@dashboard_bp.post("/dashboard/aluno/payments")
def create_student_payment():
    service = service_repository.find_by_id(request.form["service_id"])
    amount = _optional_float(request.form.get("amount"))

    if amount is None and service:
        amount = service.get("monthly_price") or 0

    payment = PaymentModel(
        student_id=request.form["student_id"],
        service_id=request.form["service_id"],
        amount=amount or 0,
        reference_month=request.form["reference_month"],
        payment_date=datetime.utcnow(),
        status="pago",
    )
    payment_repository.insert_payment(payment)

    enrollment_id = request.form.get("enrollment_id")
    if enrollment_id:
        enrollment_repository.mark_as_paid(enrollment_id)

    return redirect(url_for("dashboard.dashboard", role="aluno"))


def _classes_with_service_names(classes, services):
    services_by_id = {service["id"]: service for service in services}
    for class_model in classes:
        service = services_by_id.get(class_model.get("service_id"), {})
        class_model["service_name"] = service.get("name", "Servico nao encontrado")
        class_model["service_price"] = service.get("monthly_price")
    return classes


def _payments_with_names(payments, services, students):
    services_by_id = {service["id"]: service for service in services}
    students_by_id = {student["id"]: student for student in students}

    for payment in payments:
        service = services_by_id.get(payment.get("service_id"), {})
        student = students_by_id.get(payment.get("student_id"), {})
        payment["service_name"] = service.get("name", payment.get("service_id"))
        payment["student_name"] = student.get("name", payment.get("student_id"))

    return payments


def _enrollments_with_names(enrollments, services, classes, students):
    services_by_id = {service["id"]: service for service in services}
    classes_by_id = {class_model["id"]: class_model for class_model in classes}
    students_by_id = {student["id"]: student for student in students}

    for enrollment in enrollments:
        service = services_by_id.get(enrollment.get("service_id"), {})
        class_model = classes_by_id.get(enrollment.get("class_id"), {})
        student = students_by_id.get(enrollment.get("student_id"), {})
        enrollment["student_name"] = student.get("name", enrollment.get("student_id"))
        enrollment["service_name"] = service.get("name", "Servico nao encontrado")
        enrollment["class_schedule"] = _format_schedule(class_model)
        enrollment["service_price"] = service.get("monthly_price")

    return enrollments


def _financial_summary(payments):
    total_paid = sum(payment.get("amount") or 0 for payment in payments if payment.get("status") == "pago")
    total_pending = sum(payment.get("amount") or 0 for payment in payments if payment.get("status") != "pago")

    return {
        "total_paid": total_paid,
        "total_pending": total_pending,
        "payment_count": len(payments),
    }


def _format_schedule(class_model):
    if class_model.get("schedule_notes"):
        return class_model["schedule_notes"]
    if class_model.get("day_of_week"):
        return f"{class_model.get('day_of_week')} {class_model.get('start_time') or ''}-{class_model.get('end_time') or ''}"
    return "Horario nao informado"


def _optional_float(value):
    if value in (None, ""):
        return None
    return float(value)
