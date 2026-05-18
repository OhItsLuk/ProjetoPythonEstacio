from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any


@dataclass
class ServiceModel:
    name: str
    category: str
    service_type: str = "aula"
    monthly_price: float | None = None
    is_free: bool = False
    notes: str | None = None
    active: bool = True
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    def to_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "category": self.category,
            "service_type": self.service_type,
            "monthly_price": self.monthly_price,
            "is_free": self.is_free,
            "notes": self.notes,
            "active": self.active,
            "created_at": self.created_at,
        }
