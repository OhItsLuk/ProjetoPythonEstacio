from app.models import PaymentModel
from app.repositories.base_repository import BaseRepository


class PaymentRepository(BaseRepository):
    def __init__(self):
        super().__init__("payments")

    def insert_payment(self, payment: PaymentModel) -> str:
        return self.insert(payment.to_dict())

    def find_by_student_id(self, student_id: str) -> list[dict]:
        return self.find_by_field("student_id", student_id)

    def find_by_status(self, status: str) -> list[dict]:
        return self.find_by_field("status", status)

    def find_by_reference_month(self, reference_month: str) -> list[dict]:
        return self.find_by_field("reference_month", reference_month)
