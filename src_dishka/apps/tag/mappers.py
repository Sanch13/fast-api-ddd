from src_dishka.apps.tag.domain import TagEntity
from src_dishka.shared.dtos import TagDTOInput, TagDTOResponse
from src_dishka.apps.tag.infrastructure.models.tag import Tag as TagModel


class TagMapper:
    @staticmethod
    def dto_to_entity(dto: TagDTOInput) -> TagEntity:
        return TagEntity(
            tag=dto.tag,
        )

    @staticmethod
    def entity_to_dto(entity: TagEntity) -> TagDTOResponse:
        return TagDTOResponse(
            id=entity.id,
            tag=entity.tag,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )

    @staticmethod
    def model_to_dto(instance: TagModel) -> TagDTOResponse:
        return TagDTOResponse(
            id=instance.id,
            tag=instance.tag,
            created_at=instance.created_at,
            updated_at=instance.updated_at,
        )

    @staticmethod
    def entity_to_model(entity: TagEntity) -> TagModel:
        tag_model = TagModel(
            tag=entity.tag,
        )
        return tag_model

    @staticmethod
    def model_to_entity(instance: TagModel) -> TagEntity:
        tag_model = TagEntity(
            id=instance.id,
            tag=instance.tag,
            created_at=instance.created_at,
            updated_at=instance.updated_at,
        )
        return tag_model
