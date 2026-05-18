from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_format_resource import CustomFormatResource
    from ..models.import_rejection_resource import ImportRejectionResource
    from ..models.language import Language
    from ..models.movie_resource import MovieResource
    from ..models.quality_model import QualityModel


T = TypeVar("T", bound="ManualImportResource")


@_attrs_define
class ManualImportResource:
    """
    Attributes:
        id (Union[Unset, int]):
        path (Union[None, Unset, str]):
        relative_path (Union[None, Unset, str]):
        folder_name (Union[None, Unset, str]):
        name (Union[None, Unset, str]):
        size (Union[Unset, int]):
        movie (Union[Unset, MovieResource]):
        movie_file_id (Union[None, Unset, int]):
        release_group (Union[None, Unset, str]):
        quality (Union[Unset, QualityModel]):
        languages (Union[None, Unset, list['Language']]):
        quality_weight (Union[Unset, int]):
        download_id (Union[None, Unset, str]):
        custom_formats (Union[None, Unset, list['CustomFormatResource']]):
        custom_format_score (Union[Unset, int]):
        indexer_flags (Union[Unset, int]):
        rejections (Union[None, Unset, list['ImportRejectionResource']]):
    """

    id: Union[Unset, int] = UNSET
    path: Union[None, Unset, str] = UNSET
    relative_path: Union[None, Unset, str] = UNSET
    folder_name: Union[None, Unset, str] = UNSET
    name: Union[None, Unset, str] = UNSET
    size: Union[Unset, int] = UNSET
    movie: Union[Unset, "MovieResource"] = UNSET
    movie_file_id: Union[None, Unset, int] = UNSET
    release_group: Union[None, Unset, str] = UNSET
    quality: Union[Unset, "QualityModel"] = UNSET
    languages: Union[None, Unset, list["Language"]] = UNSET
    quality_weight: Union[Unset, int] = UNSET
    download_id: Union[None, Unset, str] = UNSET
    custom_formats: Union[None, Unset, list["CustomFormatResource"]] = UNSET
    custom_format_score: Union[Unset, int] = UNSET
    indexer_flags: Union[Unset, int] = UNSET
    rejections: Union[None, Unset, list["ImportRejectionResource"]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        path: Union[None, Unset, str]
        if isinstance(self.path, Unset):
            path = UNSET
        else:
            path = self.path

        relative_path: Union[None, Unset, str]
        if isinstance(self.relative_path, Unset):
            relative_path = UNSET
        else:
            relative_path = self.relative_path

        folder_name: Union[None, Unset, str]
        if isinstance(self.folder_name, Unset):
            folder_name = UNSET
        else:
            folder_name = self.folder_name

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        size = self.size

        movie: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.movie, Unset):
            movie = self.movie.to_dict()

        movie_file_id: Union[None, Unset, int]
        if isinstance(self.movie_file_id, Unset):
            movie_file_id = UNSET
        else:
            movie_file_id = self.movie_file_id

        release_group: Union[None, Unset, str]
        if isinstance(self.release_group, Unset):
            release_group = UNSET
        else:
            release_group = self.release_group

        quality: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.quality, Unset):
            quality = self.quality.to_dict()

        languages: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.languages, Unset):
            languages = UNSET
        elif isinstance(self.languages, list):
            languages = []
            for languages_type_0_item_data in self.languages:
                languages_type_0_item = languages_type_0_item_data.to_dict()
                languages.append(languages_type_0_item)

        else:
            languages = self.languages

        quality_weight = self.quality_weight

        download_id: Union[None, Unset, str]
        if isinstance(self.download_id, Unset):
            download_id = UNSET
        else:
            download_id = self.download_id

        custom_formats: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.custom_formats, Unset):
            custom_formats = UNSET
        elif isinstance(self.custom_formats, list):
            custom_formats = []
            for custom_formats_type_0_item_data in self.custom_formats:
                custom_formats_type_0_item = custom_formats_type_0_item_data.to_dict()
                custom_formats.append(custom_formats_type_0_item)

        else:
            custom_formats = self.custom_formats

        custom_format_score = self.custom_format_score

        indexer_flags = self.indexer_flags

        rejections: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.rejections, Unset):
            rejections = UNSET
        elif isinstance(self.rejections, list):
            rejections = []
            for rejections_type_0_item_data in self.rejections:
                rejections_type_0_item = rejections_type_0_item_data.to_dict()
                rejections.append(rejections_type_0_item)

        else:
            rejections = self.rejections

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if path is not UNSET:
            field_dict["path"] = path
        if relative_path is not UNSET:
            field_dict["relativePath"] = relative_path
        if folder_name is not UNSET:
            field_dict["folderName"] = folder_name
        if name is not UNSET:
            field_dict["name"] = name
        if size is not UNSET:
            field_dict["size"] = size
        if movie is not UNSET:
            field_dict["movie"] = movie
        if movie_file_id is not UNSET:
            field_dict["movieFileId"] = movie_file_id
        if release_group is not UNSET:
            field_dict["releaseGroup"] = release_group
        if quality is not UNSET:
            field_dict["quality"] = quality
        if languages is not UNSET:
            field_dict["languages"] = languages
        if quality_weight is not UNSET:
            field_dict["qualityWeight"] = quality_weight
        if download_id is not UNSET:
            field_dict["downloadId"] = download_id
        if custom_formats is not UNSET:
            field_dict["customFormats"] = custom_formats
        if custom_format_score is not UNSET:
            field_dict["customFormatScore"] = custom_format_score
        if indexer_flags is not UNSET:
            field_dict["indexerFlags"] = indexer_flags
        if rejections is not UNSET:
            field_dict["rejections"] = rejections

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.custom_format_resource import CustomFormatResource
        from ..models.import_rejection_resource import ImportRejectionResource
        from ..models.language import Language
        from ..models.movie_resource import MovieResource
        from ..models.quality_model import QualityModel

        # ARRSTACK_FROM_DICT_NONE_OK — upstream may return null for a
        # nullable nested object; treat it as 'no fields supplied'.
        if src_dict is None:
            return cls()
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_path(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        path = _parse_path(d.pop("path", UNSET))

        def _parse_relative_path(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        relative_path = _parse_relative_path(d.pop("relativePath", UNSET))

        def _parse_folder_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        folder_name = _parse_folder_name(d.pop("folderName", UNSET))

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        size = d.pop("size", UNSET)

        _movie = d.pop("movie", UNSET)
        movie: Union[Unset, MovieResource]
        if isinstance(_movie, Unset):
            movie = UNSET
        else:
            movie = MovieResource.from_dict(_movie)

        def _parse_movie_file_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        movie_file_id = _parse_movie_file_id(d.pop("movieFileId", UNSET))

        def _parse_release_group(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        release_group = _parse_release_group(d.pop("releaseGroup", UNSET))

        _quality = d.pop("quality", UNSET)
        quality: Union[Unset, QualityModel]
        if isinstance(_quality, Unset):
            quality = UNSET
        else:
            quality = QualityModel.from_dict(_quality)

        def _parse_languages(data: object) -> Union[None, Unset, list["Language"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                languages_type_0 = []
                _languages_type_0 = data
                for languages_type_0_item_data in _languages_type_0:
                    languages_type_0_item = Language.from_dict(
                        languages_type_0_item_data
                    )

                    languages_type_0.append(languages_type_0_item)

                return languages_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["Language"]], data)

        languages = _parse_languages(d.pop("languages", UNSET))

        quality_weight = d.pop("qualityWeight", UNSET)

        def _parse_download_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        download_id = _parse_download_id(d.pop("downloadId", UNSET))

        def _parse_custom_formats(
            data: object,
        ) -> Union[None, Unset, list["CustomFormatResource"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                custom_formats_type_0 = []
                _custom_formats_type_0 = data
                for custom_formats_type_0_item_data in _custom_formats_type_0:
                    custom_formats_type_0_item = CustomFormatResource.from_dict(
                        custom_formats_type_0_item_data
                    )

                    custom_formats_type_0.append(custom_formats_type_0_item)

                return custom_formats_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["CustomFormatResource"]], data)

        custom_formats = _parse_custom_formats(d.pop("customFormats", UNSET))

        custom_format_score = d.pop("customFormatScore", UNSET)

        indexer_flags = d.pop("indexerFlags", UNSET)

        def _parse_rejections(
            data: object,
        ) -> Union[None, Unset, list["ImportRejectionResource"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                rejections_type_0 = []
                _rejections_type_0 = data
                for rejections_type_0_item_data in _rejections_type_0:
                    rejections_type_0_item = ImportRejectionResource.from_dict(
                        rejections_type_0_item_data
                    )

                    rejections_type_0.append(rejections_type_0_item)

                return rejections_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["ImportRejectionResource"]], data)

        rejections = _parse_rejections(d.pop("rejections", UNSET))

        manual_import_resource = cls(
            id=id,
            path=path,
            relative_path=relative_path,
            folder_name=folder_name,
            name=name,
            size=size,
            movie=movie,
            movie_file_id=movie_file_id,
            release_group=release_group,
            quality=quality,
            languages=languages,
            quality_weight=quality_weight,
            download_id=download_id,
            custom_formats=custom_formats,
            custom_format_score=custom_format_score,
            indexer_flags=indexer_flags,
            rejections=rejections,
        )

        return manual_import_resource
