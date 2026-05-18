from app.models import StudentModel
from app.repositories.base_repository import BaseRepository


class StudentRepository(BaseRepository):
    def __init__(self):
        super().__init__("students")

    def insert_student(self, student: StudentModel) -> str:
        return self.insert(student.to_dict())

    def find_by_name(self, name: str) -> list[dict]:
        return self.find_by_field("name", name)

    def find_by_phone(self, phone: str) -> list[dict]:
        return self.find_by_field("phone", phone)
