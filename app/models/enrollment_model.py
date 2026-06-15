from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any


@dataclass
class EnrollmentModel:
    student_id: str
    class_id: str
    service_id: str
    status: str = "inscrito"
    payment_status: str = "pendente"
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    def to_dict(self) -> dict[str, Any]:
        return {
            "student_id": self.student_id,
            "class_id": self.class_id,
            "service_id": self.service_id,
            "status": self.status,
            "payment_status": self.payment_status,
            "created_at": self.created_at,
        }
