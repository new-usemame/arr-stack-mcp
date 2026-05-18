from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.database_locking_behavior_types import DatabaseLockingBehaviorTypes
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_database_options import CustomDatabaseOptions


T = TypeVar("T", bound="DatabaseConfigurationOptions")


@_attrs_define
class DatabaseConfigurationOptions:
    """Options to configure jellyfins managed database.

    Attributes:
        database_type (Union[Unset, str]): Gets or Sets the type of database jellyfin should use.
        custom_provider_options (Union['CustomDatabaseOptions', None, Unset]): Gets or sets the options required to use
            a custom database provider.
        locking_behavior (Union[Unset, DatabaseLockingBehaviorTypes]): Defines all possible methods for locking database
            access for concurrent queries.
    """

    database_type: Union[Unset, str] = UNSET
    custom_provider_options: Union["CustomDatabaseOptions", None, Unset] = UNSET
    locking_behavior: Union[Unset, DatabaseLockingBehaviorTypes] = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.custom_database_options import CustomDatabaseOptions

        database_type = self.database_type

        custom_provider_options: Union[None, Unset, dict[str, Any]]
        if isinstance(self.custom_provider_options, Unset):
            custom_provider_options = UNSET
        elif isinstance(self.custom_provider_options, CustomDatabaseOptions):
            custom_provider_options = self.custom_provider_options.to_dict()
        else:
            custom_provider_options = self.custom_provider_options

        locking_behavior: Union[Unset, str] = UNSET
        if not isinstance(self.locking_behavior, Unset):
            locking_behavior = self.locking_behavior.value

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if database_type is not UNSET:
            field_dict["DatabaseType"] = database_type
        if custom_provider_options is not UNSET:
            field_dict["CustomProviderOptions"] = custom_provider_options
        if locking_behavior is not UNSET:
            field_dict["LockingBehavior"] = locking_behavior

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.custom_database_options import CustomDatabaseOptions

        d = dict(src_dict)
        database_type = d.pop("DatabaseType", UNSET)

        def _parse_custom_provider_options(
            data: object,
        ) -> Union["CustomDatabaseOptions", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                custom_provider_options_type_1 = CustomDatabaseOptions.from_dict(data)

                return custom_provider_options_type_1
            except:  # noqa: E722
                pass
            return cast(Union["CustomDatabaseOptions", None, Unset], data)

        custom_provider_options = _parse_custom_provider_options(
            d.pop("CustomProviderOptions", UNSET)
        )

        _locking_behavior = d.pop("LockingBehavior", UNSET)
        locking_behavior: Union[Unset, DatabaseLockingBehaviorTypes]
        if isinstance(_locking_behavior, Unset):
            locking_behavior = UNSET
        else:
            locking_behavior = DatabaseLockingBehaviorTypes(_locking_behavior)

        database_configuration_options = cls(
            database_type=database_type,
            custom_provider_options=custom_provider_options,
            locking_behavior=locking_behavior,
        )

        return database_configuration_options
