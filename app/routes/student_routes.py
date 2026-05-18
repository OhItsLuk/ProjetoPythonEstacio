from flask import Blueprint, jsonify, request

from app.models import StudentModel
from app.repositories import StudentRepository


student_bp = Blueprint("students", __name__, url_prefix="/students")
student_repository = StudentRepository()


@student_bp.post("")
def create_student():
    data = request.get_json() or {}
    student = StudentModel(
        name=data["name"],
        phone=data.get("phone"),
        birth_date=data.get("birth_date"),
        responsible_name=data.get("responsible_name"),
        responsible_phone=data.get("responsible_phone"),
        active=data.get("active", True),
    )
    student_id = student_repository.insert_student(student)
    return jsonify({"id": student_id}), 201


@student_bp.get("")
def list_students():
    return jsonify(student_repository.find_all())


@student_bp.get("/<student_id>")
def get_student(student_id):
    student = student_repository.find_by_id(student_id)
    if not student:
        return jsonify({"message": "Aluno nao encontrado."}), 404

    return jsonify(student)


@student_bp.get("/search")
def search_students():
    name = request.args.get("name")
    phone = request.args.get("phone")

    if name:
        return jsonify(student_repository.find_by_name(name))
    if phone:
        return jsonify(student_repository.find_by_phone(phone))

    return jsonify(student_repository.find_all())
