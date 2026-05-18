from flask import Blueprint, jsonify, request

from app.models import ServiceModel
from app.repositories import ServiceRepository


service_bp = Blueprint("services", __name__, url_prefix="/services")
service_repository = ServiceRepository()


@service_bp.post("")
def create_service():
    data = request.get_json() or {}
    service = ServiceModel(
        name=data["name"],
        category=data["category"],
        service_type=data.get("service_type", "aula"),
        monthly_price=data.get("monthly_price"),
        is_free=data.get("is_free", False),
        notes=data.get("notes"),
        active=data.get("active", True),
    )
    service_id = service_repository.insert_service(service)
    return jsonify({"id": service_id}), 201


@service_bp.get("")
def list_services():
    return jsonify(service_repository.find_all())


@service_bp.get("/<service_id>")
def get_service(service_id):
    service = service_repository.find_by_id(service_id)
    if not service:
        return jsonify({"message": "Servico nao encontrado."}), 404

    return jsonify(service)


@service_bp.get("/search")
def search_services():
    name = request.args.get("name")
    category = request.args.get("category")
    service_type = request.args.get("type")
    free = request.args.get("free")

    if name:
        return jsonify(service_repository.find_by_name(name))
    if category:
        return jsonify(service_repository.find_by_category(category))
    if service_type:
        return jsonify(service_repository.find_by_type(service_type))
    if free and free.lower() == "true":
        return jsonify(service_repository.find_free_services())

    return jsonify(service_repository.find_all())
