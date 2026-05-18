from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any


@dataclass
class ClassModel:
    service_id: str
    day_of_week: str | None = None
    start_time: str | None = None
    end_time: str | None = None
    professional_id: str | None = None
    capacity: int | None = None
    schedule_notes: str | None = None
    active: bool = True
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    def to_dict(self) -> dict[str, Any]:
        return {
            "service_id": self.service_id,
            "day_of_week": self.day_of_week,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "professional_id": self.professional_id,
            "capacity": self.capacity,
            "schedule_notes": self.schedule_notes,
            "active": self.active,
            "created_at": self.created_at,
        }
