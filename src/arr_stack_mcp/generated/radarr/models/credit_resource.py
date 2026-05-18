from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.credit_type import CreditType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.media_cover import MediaCover


T = TypeVar("T", bound="CreditResource")


@_attrs_define
class CreditResource:
    """
    Attributes:
        id (Union[Unset, int]):
        person_name (Union[None, Unset, str]):
        credit_tmdb_id (Union[None, Unset, str]):
        person_tmdb_id (Union[Unset, int]):
        movie_metadata_id (Union[Unset, int]):
        images (Union[None, Unset, list['MediaCover']]):
        department (Union[None, Unset, str]):
        job (Union[None, Unset, str]):
        character (Union[None, Unset, str]):
        order (Union[Unset, int]):
        type_ (Union[Unset, CreditType]):
    """

    id: Union[Unset, int] = UNSET
    person_name: Union[None, Unset, str] = UNSET
    credit_tmdb_id: Union[None, Unset, str] = UNSET
    person_tmdb_id: Union[Unset, int] = UNSET
    movie_metadata_id: Union[Unset, int] = UNSET
    images: Union[None, Unset, list["MediaCover"]] = UNSET
    department: Union[None, Unset, str] = UNSET
    job: Union[None, Unset, str] = UNSET
    character: Union[None, Unset, str] = UNSET
    order: Union[Unset, int] = UNSET
    type_: Union[Unset, CreditType] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        person_name: Union[None, Unset, str]
        if isinstance(self.person_name, Unset):
            person_name = UNSET
        else:
            person_name = self.person_name

        credit_tmdb_id: Union[None, Unset, str]
        if isinstance(self.credit_tmdb_id, Unset):
            credit_tmdb_id = UNSET
        else:
            credit_tmdb_id = self.credit_tmdb_id

        person_tmdb_id = self.person_tmdb_id

        movie_metadata_id = self.movie_metadata_id

        images: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.images, Unset):
            images = UNSET
        elif isinstance(self.images, list):
            images = []
            for images_type_0_item_data in self.images:
                images_type_0_item = images_type_0_item_data.to_dict()
                images.append(images_type_0_item)

        else:
            images = self.images

        department: Union[None, Unset, str]
        if isinstance(self.department, Unset):
            department = UNSET
        else:
            department = self.department

        job: Union[None, Unset, str]
        if isinstance(self.job, Unset):
            job = UNSET
        else:
            job = self.job

        character: Union[None, Unset, str]
        if isinstance(self.character, Unset):
            character = UNSET
        else:
            character = self.character

        order = self.order

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if person_name is not UNSET:
            field_dict["personName"] = person_name
        if credit_tmdb_id is not UNSET:
            field_dict["creditTmdbId"] = credit_tmdb_id
        if person_tmdb_id is not UNSET:
            field_dict["personTmdbId"] = person_tmdb_id
        if movie_metadata_id is not UNSET:
            field_dict["movieMetadataId"] = movie_metadata_id
        if images is not UNSET:
            field_dict["images"] = images
        if department is not UNSET:
            field_dict["department"] = department
        if job is not UNSET:
            field_dict["job"] = job
        if character is not UNSET:
            field_dict["character"] = character
        if order is not UNSET:
            field_dict["order"] = order
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.media_cover import MediaCover

        # ARRSTACK_FROM_DICT_NONE_OK — upstream may return null for a
        # nullable nested object; treat it as 'no fields supplied'.
        if src_dict is None:
            return cls()
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_person_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        person_name = _parse_person_name(d.pop("personName", UNSET))

        def _parse_credit_tmdb_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        credit_tmdb_id = _parse_credit_tmdb_id(d.pop("creditTmdbId", UNSET))

        person_tmdb_id = d.pop("personTmdbId", UNSET)

        movie_metadata_id = d.pop("movieMetadataId", UNSET)

        def _parse_images(data: object) -> Union[None, Unset, list["MediaCover"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                images_type_0 = []
                _images_type_0 = data
                for images_type_0_item_data in _images_type_0:
                    images_type_0_item = MediaCover.from_dict(images_type_0_item_data)

                    images_type_0.append(images_type_0_item)

                return images_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["MediaCover"]], data)

        images = _parse_images(d.pop("images", UNSET))

        def _parse_department(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        department = _parse_department(d.pop("department", UNSET))

        def _parse_job(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        job = _parse_job(d.pop("job", UNSET))

        def _parse_character(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        character = _parse_character(d.pop("character", UNSET))

        order = d.pop("order", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, CreditType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = CreditType(_type_)

        credit_resource = cls(
            id=id,
            person_name=person_name,
            credit_tmdb_id=credit_tmdb_id,
            person_tmdb_id=person_tmdb_id,
            movie_metadata_id=movie_metadata_id,
            images=images,
            department=department,
            job=job,
            character=character,
            order=order,
            type_=type_,
        )

        return credit_resource
