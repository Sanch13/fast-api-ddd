from src.apps.tag.domain import TagEntity
from src.shared.dtos import TagDTO


class TagMapper:
    @staticmethod
    def dto_to_entity(dto: TagDTO) -> TagEntity:
        return TagEntity(
            tag=dto.tag
        )

    @staticmethod
    def entity_to_dto(entity: TagEntity) -> TagDTO:
        return TagDTO(

            tag=entity.tag,
        )
