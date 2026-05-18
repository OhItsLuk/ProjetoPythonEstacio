from app.models import ServiceModel
from app.repositories.base_repository import BaseRepository


class ServiceRepository(BaseRepository):
    def __init__(self):
        super().__init__("services")

    def insert_service(self, service: ServiceModel) -> str:
        return self.insert(service.to_dict())

    def find_by_name(self, name: str) -> list[dict]:
        return self.find_by_field("name", name)

    def find_by_category(self, category: str) -> list[dict]:
        return self.find_by_field("category", category)

    def find_by_type(self, service_type: str) -> list[dict]:
        return self.find_by_field("service_type", service_type)

    def find_free_services(self) -> list[dict]:
        return self.find_by_field("is_free", True)
