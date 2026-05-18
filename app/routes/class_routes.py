from flask import Blueprint, jsonify, request

from app.models import ClassModel
from app.repositories import ClassRepository


class_bp = Blueprint("classes", __name__, url_prefix="/classes")
class_repository = ClassRepository()


@class_bp.post("")
def create_class():
    data = request.get_json() or {}
    class_model = ClassModel(
        service_id=data["service_id"],
        day_of_week=data.get("day_of_week"),
        start_time=data.get("start_time"),
        end_time=data.get("end_time"),
        professional_id=data.get("professional_id"),
        capacity=data.get("capacity"),
        schedule_notes=data.get("schedule_notes"),
        active=data.get("active", True),
    )
    class_id = class_repository.insert_class(class_model)
    return jsonify({"id": class_id}), 201


@class_bp.get("")
def list_classes():
    return jsonify(class_repository.find_all())


@class_bp.get("/<class_id>")
def get_class(class_id):
    class_model = class_repository.find_by_id(class_id)
    if not class_model:
        return jsonify({"message": "Aula nao encontrada."}), 404

    return jsonify(class_model)


@class_bp.get("/search")
def search_classes():
    service_id = request.args.get("service_id")
    day_of_week = request.args.get("day_of_week")

    if service_id:
        return jsonify(class_repository.find_by_service_id(service_id))
    if day_of_week:
        return jsonify(class_repository.find_by_day_of_week(day_of_week))

    return jsonify(class_repository.find_all())
