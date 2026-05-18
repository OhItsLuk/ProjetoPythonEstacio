from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any


@dataclass
class PaymentModel:
    student_id: str
    service_id: str
    amount: float
    reference_month: str
    payment_date: datetime | None = None
    status: str = "pendente"
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    def to_dict(self) -> dict[str, Any]:
        return {
            "student_id": self.student_id,
            "service_id": self.service_id,
            "amount": self.amount,
            "reference_month": self.reference_month,
            "payment_date": self.payment_date,
            "status": self.status,
            "created_at": self.created_at,
        }
