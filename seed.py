from datetime import datetime

from app.models import (
    ClassModel,
    EnrollmentModel,
    PaymentModel,
    ProfessionalModel,
    ServiceModel,
    StudentModel,
    UserModel,
)
from app.repositories import (
    ClassRepository,
    EnrollmentRepository,
    PaymentRepository,
    ProfessionalRepository,
    ServiceRepository,
    StudentRepository,
    UserRepository,
)


services_data = [
    {
        "name": "Jiu-Jitsu",
        "category": "Saude e bem-estar",
        "monthly_price": 30.00,
        "schedules": [
            ("Terca", "19:00", "20:30"),
            ("Quinta", "19:00", "20:30"),
        ],
    },
    {
        "name": "Mat Pilates",
        "category": "Saude e bem-estar",
        "monthly_price": 30.00,
        "schedules": [
            ("Terca", "09:30", "10:30"),
            ("Quinta", "09:30", "10:30"),
            ("Terca", "17:00", "18:00"),
            ("Quinta", "17:00", "18:00"),
        ],
    },
    {
        "name": "Ginastica",
        "category": "Saude e bem-estar",
        "monthly_price": 35.00,
        "schedules": [
            ("Quarta", "08:00", "09:00"),
            ("Sexta", "08:00", "09:00"),
        ],
    },
    {
        "name": "Iogaterapia",
        "category": "Saude e bem-estar",
        "monthly_price": 25.00,
        "schedules": [("Sexta", "17:00", "19:00")],
    },
    {
        "name": "Danca Mix",
        "category": "Danca e expressao corporal",
        "monthly_price": 20.00,
        "schedules": [("Segunda", "09:00", "10:00")],
    },
    {
        "name": "Aula de K-POP",
        "category": "Danca e expressao corporal",
        "monthly_price": 30.00,
        "schedules": [("Sabado", "15:00", "16:30")],
    },
    {
        "name": "Bale",
        "category": "Danca e expressao corporal",
        "monthly_price": 40.00,
        "schedule_notes": "Dias e horarios a confirmar",
    },
    {
        "name": "Alfabetizacao e Letramento",
        "category": "Educacao e idiomas",
        "monthly_price": 50.00,
        "schedules": [
            ("Segunda", "08:30", "10:00"),
            ("Segunda", "10:00", "11:30"),
            ("Quarta", "17:30", "19:00"),
        ],
    },
    {
        "name": "Curso de Espanhol basico",
        "category": "Educacao e idiomas",
        "monthly_price": 30.00,
        "service_type": "curso",
        "schedules": [("Terca", "14:00", "15:30")],
    },
    {
        "name": "Curso de Esperanto basico",
        "category": "Educacao e idiomas",
        "monthly_price": 0.00,
        "is_free": True,
        "service_type": "curso",
        "schedules": [("Sabado", "09:00", "10:30")],
    },
    {
        "name": "Curso de Ingles basico",
        "category": "Educacao e idiomas",
        "monthly_price": 30.00,
        "service_type": "curso",
        "schedules": [("Sabado", "10:30", "12:00")],
    },
    {
        "name": "Curso de desenho",
        "category": "Cultura e artes",
        "monthly_price": 60.00,
        "service_type": "curso",
        "schedules": [("Segunda", "13:00", "15:00")],
    },
    {
        "name": "Curso de tranca",
        "category": "Cultura e artes",
        "monthly_price": 50.00,
        "service_type": "curso",
        "schedules": [("Terca", "14:00", "16:30")],
    },
    {
        "name": "Curso de croche",
        "category": "Cultura e artes",
        "monthly_price": 10.00,
        "service_type": "curso",
        "schedules": [("Terca", "15:00", "17:00")],
    },
    {
        "name": "Aula de artesanato",
        "category": "Cultura e artes",
        "monthly_price": 0.00,
        "is_free": True,
        "schedules": [("Terca", "15:00", "17:00")],
    },
    {
        "name": "Aula de violao",
        "category": "Cultura e artes",
        "monthly_price": 30.00,
        "schedules": [("Sabado", "09:00", "10:30")],
    },
    {
        "name": "Extensao de cilios, higienizacao capilar e escovacao",
        "category": "Servicos de beleza",
        "service_type": "servico",
        "notes": "Dias, horarios e valores confirmar no WhatsApp.",
        "schedule_notes": "Dias e horarios a confirmar",
    },
]


students_data = [
    {
        "name": "Ana Clara Souza",
        "phone": "21982020001",
        "birth_date": "2012-04-15",
        "responsible_name": "Mariana Souza",
        "responsible_phone": "21982029901",
    },
    {
        "name": "Bruno Lima",
        "phone": "21982020002",
        "birth_date": "2009-11-03",
        "responsible_name": "Carlos Lima",
        "responsible_phone": "21982029902",
    },
    {
        "name": "Camila Rocha",
        "phone": "21982020003",
        "birth_date": "1998-07-21",
    },
    {
        "name": "Diego Santos",
        "phone": "21982020004",
        "birth_date": "1987-02-10",
    },
]


professionals_data = [
    {
        "name": "Prof. Juliana Martins",
        "phone": "21982021001",
        "email": "juliana.martins@ong.local",
        "specialty": "Danca e expressao corporal",
    },
    {
        "name": "Prof. Renato Alves",
        "phone": "21982021002",
        "email": "renato.alves@ong.local",
        "specialty": "Educacao e idiomas",
    },
    {
        "name": "Prof. Patricia Nunes",
        "phone": "21982021003",
        "email": "patricia.nunes@ong.local",
        "specialty": "Cultura e artes",
    },
]


users_data = [
    {
        "name": "Administrador Geral",
        "email": "admin@ong.local",
        "role": "admin",
        "password": "admin123",
    },
    {
        "name": "Prof. Juliana Martins",
        "email": "juliana.martins@ong.local",
        "role": "professor",
        "password": "prof123",
        "related_name": "Prof. Juliana Martins",
        "related_type": "professional",
    },
    {
        "name": "Prof. Renato Alves",
        "email": "renato.alves@ong.local",
        "role": "professor",
        "password": "prof123",
        "related_name": "Prof. Renato Alves",
        "related_type": "professional",
    },
    {
        "name": "Ana Clara Souza",
        "email": "ana.clara@ong.local",
        "role": "aluno",
        "password": "aluno123",
        "related_name": "Ana Clara Souza",
        "related_type": "student",
    },
    {
        "name": "Bruno Lima",
        "email": "bruno.lima@ong.local",
        "role": "aluno",
        "password": "aluno123",
        "related_name": "Bruno Lima",
        "related_type": "student",
    },
]


enrollments_data = [
    {"student_name": "Ana Clara Souza", "service_name": "Aula de K-POP", "payment_status": "pago"},
    {"student_name": "Ana Clara Souza", "service_name": "Curso de Ingles basico", "payment_status": "pendente"},
    {"student_name": "Bruno Lima", "service_name": "Jiu-Jitsu", "payment_status": "pago"},
    {"student_name": "Camila Rocha", "service_name": "Curso de desenho", "payment_status": "pago"},
    {"student_name": "Diego Santos", "service_name": "Mat Pilates", "payment_status": "pendente"},
]


payments_data = [
    {"student_name": "Ana Clara Souza", "service_name": "Aula de K-POP", "amount": 30.00, "status": "pago"},
    {"student_name": "Ana Clara Souza", "service_name": "Curso de Ingles basico", "amount": 30.00, "status": "pendente"},
    {"student_name": "Bruno Lima", "service_name": "Jiu-Jitsu", "amount": 30.00, "status": "pago"},
    {"student_name": "Camila Rocha", "service_name": "Curso de desenho", "amount": 60.00, "status": "pago"},
    {"student_name": "Diego Santos", "service_name": "Mat Pilates", "amount": 30.00, "status": "pendente"},
]


def build_dashboard_preview_data():
    services = []
    classes = []

    for service_index, service_data in enumerate(services_data, start=1):
        service_id = f"mock-service-{service_index}"
        services.append(
            {
                "id": service_id,
                "name": service_data["name"],
                "category": service_data["category"],
                "service_type": service_data.get("service_type", "aula"),
                "monthly_price": service_data.get("monthly_price"),
                "is_free": service_data.get("is_free", False),
                "notes": service_data.get("notes"),
                "active": True,
            }
        )

        for class_index, schedule in enumerate(service_data.get("schedules", []), start=1):
            day_of_week, start_time, end_time = schedule
            classes.append(
                {
                    "id": f"mock-class-{service_index}-{class_index}",
                    "service_id": service_id,
                    "day_of_week": day_of_week,
                    "start_time": start_time,
                    "end_time": end_time,
                    "schedule_notes": None,
                    "active": True,
                }
            )

        if service_data.get("schedule_notes"):
            classes.append(
                {
                    "id": f"mock-class-{service_index}-notes",
                    "service_id": service_id,
                    "day_of_week": None,
                    "start_time": None,
                    "end_time": None,
                    "schedule_notes": service_data["schedule_notes"],
                    "active": True,
                }
            )

    students = [
        {"id": f"mock-student-{index}", **student_data}
        for index, student_data in enumerate(students_data, start=1)
    ]
    professionals = [
        {"id": f"mock-professional-{index}", **professional_data}
        for index, professional_data in enumerate(professionals_data, start=1)
    ]

    students_by_name = {student["name"]: student for student in students}
    professionals_by_name = {professional["name"]: professional for professional in professionals}
    services_by_name = {service["name"]: service for service in services}
    first_class_by_service_id = {}
    for class_model in classes:
        first_class_by_service_id.setdefault(class_model["service_id"], class_model)

    users = []
    for index, user_data in enumerate(users_data, start=1):
        related_id = None
        if user_data.get("related_type") == "student":
            related_id = students_by_name[user_data["related_name"]]["id"]
        if user_data.get("related_type") == "professional":
            related_id = professionals_by_name[user_data["related_name"]]["id"]

        users.append(
            {
                "id": f"mock-user-{index}",
                "name": user_data["name"],
                "email": user_data["email"],
                "role": user_data["role"],
                "related_id": related_id,
                "active": True,
            }
        )

    enrollments = []
    for index, enrollment_data in enumerate(enrollments_data, start=1):
        student = students_by_name[enrollment_data["student_name"]]
        service = services_by_name[enrollment_data["service_name"]]
        class_model = first_class_by_service_id[service["id"]]
        enrollments.append(
            {
                "id": f"mock-enrollment-{index}",
                "student_id": student["id"],
                "class_id": class_model["id"],
                "service_id": service["id"],
                "status": "inscrito",
                "payment_status": enrollment_data["payment_status"],
            }
        )

    payments = []
    for index, payment_data in enumerate(payments_data, start=1):
        student = students_by_name[payment_data["student_name"]]
        service = services_by_name[payment_data["service_name"]]
        payments.append(
            {
                "id": f"mock-payment-{index}",
                "student_id": student["id"],
                "service_id": service["id"],
                "amount": payment_data["amount"],
                "reference_month": "2026-06",
                "status": payment_data["status"],
            }
        )

    return {
        "services": services,
        "classes": classes,
        "students": students,
        "professionals": professionals,
        "users": users,
        "enrollments": enrollments,
        "payments": payments,
    }


def seed_services_and_classes():
    service_repository = ServiceRepository()
    class_repository = ClassRepository()

    for service_data in services_data:
        existing_service = service_repository.find_by_name(service_data["name"])
        if existing_service:
            service_id = existing_service[0]["id"]
        else:
            service = ServiceModel(
                name=service_data["name"],
                category=service_data["category"],
                service_type=service_data.get("service_type", "aula"),
                monthly_price=service_data.get("monthly_price"),
                is_free=service_data.get("is_free", False),
                notes=service_data.get("notes"),
            )
            service_id = service_repository.insert_service(service)

        if class_repository.find_by_service_id(service_id):
            continue

        schedules = service_data.get("schedules", [])
        for day_of_week, start_time, end_time in schedules:
            class_repository.insert_class(
                ClassModel(
                    service_id=service_id,
                    day_of_week=day_of_week,
                    start_time=start_time,
                    end_time=end_time,
                )
            )

        schedule_notes = service_data.get("schedule_notes")
        if schedule_notes:
            class_repository.insert_class(
                ClassModel(service_id=service_id, schedule_notes=schedule_notes)
            )


def seed_mock_dashboard_data():
    seed_services_and_classes()

    student_repository = StudentRepository()
    professional_repository = ProfessionalRepository()
    user_repository = UserRepository()
    service_repository = ServiceRepository()
    class_repository = ClassRepository()
    enrollment_repository = EnrollmentRepository()
    payment_repository = PaymentRepository()

    students_by_name = {}
    for student_data in students_data:
        student_id = _get_or_create_student(student_repository, student_data)
        students_by_name[student_data["name"]] = student_id

    professionals_by_name = {}
    for professional_data in professionals_data:
        professional_id = _get_or_create_professional(professional_repository, professional_data)
        professionals_by_name[professional_data["name"]] = professional_id

    for user_data in users_data:
        related_id = None
        if user_data.get("related_type") == "student":
            related_id = students_by_name.get(user_data.get("related_name"))
        if user_data.get("related_type") == "professional":
            related_id = professionals_by_name.get(user_data.get("related_name"))

        _get_or_create_user(user_repository, user_data, related_id)

    services_by_name = {
        service["name"]: service
        for service in service_repository.find_all()
    }
    classes_by_service_id = {}
    for class_model in class_repository.find_all():
        classes_by_service_id.setdefault(class_model["service_id"], class_model)

    for enrollment_data in enrollments_data:
        student_id = students_by_name[enrollment_data["student_name"]]
        service = services_by_name[enrollment_data["service_name"]]
        class_model = classes_by_service_id.get(service["id"])
        if not class_model:
            continue

        _get_or_create_enrollment(
            enrollment_repository,
            student_id=student_id,
            class_id=class_model["id"],
            service_id=service["id"],
            payment_status=enrollment_data["payment_status"],
        )

    for payment_data in payments_data:
        student_id = students_by_name[payment_data["student_name"]]
        service = services_by_name[payment_data["service_name"]]
        _get_or_create_payment(
            payment_repository,
            student_id=student_id,
            service_id=service["id"],
            amount=payment_data["amount"],
            status=payment_data["status"],
            reference_month="2026-06",
        )


def _get_or_create_student(repository, student_data):
    existing = repository.find_by_name(student_data["name"])
    if existing:
        return existing[0]["id"]

    return repository.insert_student(StudentModel(**student_data))


def _get_or_create_professional(repository, professional_data):
    existing = repository.find_by_email(professional_data["email"])
    if existing:
        return existing[0]["id"]

    return repository.insert_professional(ProfessionalModel(**professional_data))


def _get_or_create_user(repository, user_data, related_id):
    existing = repository.find_by_email(user_data["email"])
    if existing:
        return existing[0]["id"]

    user = UserModel(
        name=user_data["name"],
        email=user_data["email"],
        role=user_data["role"],
        password=user_data["password"],
        related_id=related_id,
    )
    return repository.insert_user(user)


def _get_or_create_enrollment(
    repository,
    student_id,
    class_id,
    service_id,
    payment_status,
):
    existing = [
        enrollment
        for enrollment in repository.find_by_student_id(student_id)
        if enrollment.get("class_id") == class_id
    ]
    if existing:
        return existing[0]["id"]

    enrollment = EnrollmentModel(
        student_id=student_id,
        class_id=class_id,
        service_id=service_id,
        payment_status=payment_status,
    )
    return repository.insert_enrollment(enrollment)


def _get_or_create_payment(
    repository,
    student_id,
    service_id,
    amount,
    status,
    reference_month,
):
    existing = [
        payment
        for payment in repository.find_by_student_id(student_id)
        if payment.get("service_id") == service_id
        and payment.get("reference_month") == reference_month
    ]
    if existing:
        return existing[0]["id"]

    payment = PaymentModel(
        student_id=student_id,
        service_id=service_id,
        amount=amount,
        reference_month=reference_month,
        payment_date=datetime.utcnow() if status == "pago" else None,
        status=status,
    )
    return repository.insert_payment(payment)


if __name__ == "__main__":
    seed_mock_dashboard_data()
    print("Mocks do dashboard cadastrados com sucesso.")
