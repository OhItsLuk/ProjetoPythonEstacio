from app.models import ClassModel
from app.repositories.base_repository import BaseRepository


class ClassRepository(BaseRepository):
    def __init__(self):
        super().__init__("classes")

    def insert_class(self, class_model: ClassModel) -> str:
        return self.insert(class_model.to_dict())

    def find_by_service_id(self, service_id: str) -> list[dict]:
        return self.find_by_field("service_id", service_id)

    def find_by_day_of_week(self, day_of_week: str) -> list[dict]:
        return self.find_by_field("day_of_week", day_of_week)
