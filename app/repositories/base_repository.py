from typing import Any

from bson import ObjectId

from app.database import get_collection


class BaseRepository:
    def __init__(self, collection_name: str):
        self.collection = get_collection(collection_name)

    def insert(self, data: dict[str, Any]) -> str:
        result = self.collection.insert_one(data)
        return str(result.inserted_id)

    def find_all(self) -> list[dict[str, Any]]:
        return [self._serialize(document) for document in self.collection.find()]

    def find_by_id(self, document_id: str) -> dict[str, Any] | None:
        if not ObjectId.is_valid(document_id):
            return None

        document = self.collection.find_one({"_id": ObjectId(document_id)})
        return self._serialize(document) if document else None

    def find_by_field(self, field_name: str, value: Any) -> list[dict[str, Any]]:
        return [
            self._serialize(document)
            for document in self.collection.find({field_name: value})
        ]

    def update_by_id(self, document_id: str, data: dict[str, Any]) -> bool:
        if not ObjectId.is_valid(document_id):
            return False

        result = self.collection.update_one(
            {"_id": ObjectId(document_id)},
            {"$set": data},
        )
        return result.modified_count > 0

    def _serialize(self, document: dict[str, Any]) -> dict[str, Any]:
        document["id"] = str(document.pop("_id"))
        return document
