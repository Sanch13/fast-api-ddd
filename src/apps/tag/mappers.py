from src.apps.tag.domain import TagEntity
from src.shared.dtos import TagDTOInput, TagDTOResponse
from src.apps.tag.infrastructure.models.tag import Tag as TagModel


class TagMapper:
    @staticmethod
    def dto_to_entity(dto: TagDTOInput) -> TagEntity:
        return TagEntity(
            tag=dto.tag
        )

    @staticmethod
    def entity_to_dto(entity: TagEntity) -> TagDTOInput:
        return TagDTOInput(
            tag=entity.tag,
        )

    @staticmethod
    def model_to_dto(instance: TagModel):
        return TagDTOResponse(
            id=instance.id,
            tag=instance.tag,
            created_at=instance.created_at,
            updated_at=instance.updated_at,
        )
