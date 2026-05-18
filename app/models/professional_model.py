from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any


@dataclass
class ProfessionalModel:
    name: str
    phone: str | None = None
    email: str | None = None
    specialty: str | None = None
    active: bool = True
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    def to_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "specialty": self.specialty,
            "active": self.active,
            "created_at": self.created_at,
        }
