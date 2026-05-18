from flask import Blueprint, jsonify, request

from app.models import PaymentModel
from app.repositories import PaymentRepository


payment_bp = Blueprint("payments", __name__, url_prefix="/payments")
payment_repository = PaymentRepository()


@payment_bp.post("")
def create_payment():
    data = request.get_json() or {}
    payment = PaymentModel(
        student_id=data["student_id"],
        service_id=data["service_id"],
        amount=data["amount"],
        reference_month=data["reference_month"],
        payment_date=data.get("payment_date"),
        status=data.get("status", "pendente"),
    )
    payment_id = payment_repository.insert_payment(payment)
    return jsonify({"id": payment_id}), 201


@payment_bp.get("")
def list_payments():
    return jsonify(payment_repository.find_all())


@payment_bp.get("/<payment_id>")
def get_payment(payment_id):
    payment = payment_repository.find_by_id(payment_id)
    if not payment:
        return jsonify({"message": "Pagamento nao encontrado."}), 404

    return jsonify(payment)


@payment_bp.get("/search")
def search_payments():
    student_id = request.args.get("student_id")
    status = request.args.get("status")
    reference_month = request.args.get("reference_month")

    if student_id:
        return jsonify(payment_repository.find_by_student_id(student_id))
    if status:
        return jsonify(payment_repository.find_by_status(status))
    if reference_month:
        return jsonify(payment_repository.find_by_reference_month(reference_month))

    return jsonify(payment_repository.find_all())
