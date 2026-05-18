from flask import Blueprint, jsonify, request

from app.models import ProfessionalModel
from app.repositories import ProfessionalRepository


professional_bp = Blueprint("professionals", __name__, url_prefix="/professionals")
professional_repository = ProfessionalRepository()


@professional_bp.post("")
def create_professional():
    data = request.get_json() or {}
    professional = ProfessionalModel(
        name=data["name"],
        phone=data.get("phone"),
        email=data.get("email"),
        specialty=data.get("specialty"),
        active=data.get("active", True),
    )
    professional_id = professional_repository.insert_professional(professional)
    return jsonify({"id": professional_id}), 201


@professional_bp.get("")
def list_professionals():
    return jsonify(professional_repository.find_all())


@professional_bp.get("/<professional_id>")
def get_professional(professional_id):
    professional = professional_repository.find_by_id(professional_id)
    if not professional:
        return jsonify({"message": "Profissional nao encontrado."}), 404

    return jsonify(professional)


@professional_bp.get("/search")
def search_professionals():
    name = request.args.get("name")
    specialty = request.args.get("specialty")

    if name:
        return jsonify(professional_repository.find_by_name(name))
    if specialty:
        return jsonify(professional_repository.find_by_specialty(specialty))

    return jsonify(professional_repository.find_all())
