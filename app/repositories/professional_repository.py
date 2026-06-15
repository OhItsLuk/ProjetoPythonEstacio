from app.models import ProfessionalModel
from app.repositories.base_repository import BaseRepository


class ProfessionalRepository(BaseRepository):
    def __init__(self):
        super().__init__("professionals")

    def insert_professional(self, professional: ProfessionalModel) -> str:
        return self.insert(professional.to_dict())

    def find_by_name(self, name: str) -> list[dict]:
        return self.find_by_field("name", name)

    def find_by_email(self, email: str) -> list[dict]:
        return self.find_by_field("email", email)

    def find_by_specialty(self, specialty: str) -> list[dict]:
        return self.find_by_field("specialty", specialty)
