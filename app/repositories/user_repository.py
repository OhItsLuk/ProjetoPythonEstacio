from app.models import UserModel
from app.repositories.base_repository import BaseRepository


class UserRepository(BaseRepository):
    def __init__(self):
        super().__init__("users")

    def insert_user(self, user: UserModel) -> str:
        return self.insert(user.to_dict())

    def find_by_email(self, email: str) -> list[dict]:
        return self.find_by_field("email", email)

    def find_by_role(self, role: str) -> list[dict]:
        return self.find_by_field("role", role)

    def update_role(self, user_id: str, role: str) -> bool:
        return self.update_by_id(user_id, {"role": role})
