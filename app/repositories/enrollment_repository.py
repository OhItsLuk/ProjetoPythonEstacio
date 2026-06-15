from app.models import EnrollmentModel
from app.repositories.base_repository import BaseRepository


class EnrollmentRepository(BaseRepository):
    def __init__(self):
        super().__init__("enrollments")

    def insert_enrollment(self, enrollment: EnrollmentModel) -> str:
        return self.insert(enrollment.to_dict())

    def find_by_student_id(self, student_id: str) -> list[dict]:
        return self.find_by_field("student_id", student_id)

    def find_by_class_id(self, class_id: str) -> list[dict]:
        return self.find_by_field("class_id", class_id)

    def find_by_service_id(self, service_id: str) -> list[dict]:
        return self.find_by_field("service_id", service_id)

    def mark_as_paid(self, enrollment_id: str) -> bool:
        return self.update_by_id(enrollment_id, {"payment_status": "pago"})
