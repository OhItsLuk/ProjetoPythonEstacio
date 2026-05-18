from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any


@dataclass
class StudentModel:
    name: str
    phone: str | None = None
    birth_date: str | None = None
    responsible_name: str | None = None
    responsible_phone: str | None = None
    active: bool = True
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    def to_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "phone": self.phone,
            "birth_date": self.birth_date,
            "responsible_name": self.responsible_name,
            "responsible_phone": self.responsible_phone,
            "active": self.active,
            "created_at": self.created_at,
        }
