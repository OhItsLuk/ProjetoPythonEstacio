from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any

from werkzeug.security import generate_password_hash


@dataclass
class UserModel:
    name: str
    email: str
    role: str
    password: str
    related_id: str | None = None
    active: bool = True
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    def to_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "email": self.email,
            "role": self.role,
            "password_hash": generate_password_hash(self.password),
            "related_id": self.related_id,
            "active": self.active,
            "created_at": self.created_at,
        }
