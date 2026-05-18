import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="LogResource")


@_attrs_define
class LogResource:
    """
    Attributes:
        id (Union[Unset, int]):
        time (Union[Unset, datetime.datetime]):
        exception (Union[None, Unset, str]):
        exception_type (Union[None, Unset, str]):
        level (Union[None, Unset, str]):
        logger (Union[None, Unset, str]):
        message (Union[None, Unset, str]):
        method (Union[None, Unset, str]):
    """

    id: Union[Unset, int] = UNSET
    time: Union[Unset, datetime.datetime] = UNSET
    exception: Union[None, Unset, str] = UNSET
    exception_type: Union[None, Unset, str] = UNSET
    level: Union[None, Unset, str] = UNSET
    logger: Union[None, Unset, str] = UNSET
    message: Union[None, Unset, str] = UNSET
    method: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        time: Union[Unset, str] = UNSET
        if not isinstance(self.time, Unset):
            time = self.time.isoformat()

        exception: Union[None, Unset, str]
        if isinstance(self.exception, Unset):
            exception = UNSET
        else:
            exception = self.exception

        exception_type: Union[None, Unset, str]
        if isinstance(self.exception_type, Unset):
            exception_type = UNSET
        else:
            exception_type = self.exception_type

        level: Union[None, Unset, str]
        if isinstance(self.level, Unset):
            level = UNSET
        else:
            level = self.level

        logger: Union[None, Unset, str]
        if isinstance(self.logger, Unset):
            logger = UNSET
        else:
            logger = self.logger

        message: Union[None, Unset, str]
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        method: Union[None, Unset, str]
        if isinstance(self.method, Unset):
            method = UNSET
        else:
            method = self.method

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if time is not UNSET:
            field_dict["time"] = time
        if exception is not UNSET:
            field_dict["exception"] = exception
        if exception_type is not UNSET:
            field_dict["exceptionType"] = exception_type
        if level is not UNSET:
            field_dict["level"] = level
        if logger is not UNSET:
            field_dict["logger"] = logger
        if message is not UNSET:
            field_dict["message"] = message
        if method is not UNSET:
            field_dict["method"] = method

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _time = d.pop("time", UNSET)
        time: Union[Unset, datetime.datetime]
        if isinstance(_time, Unset):
            time = UNSET
        else:
            time = isoparse(_time)

        def _parse_exception(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        exception = _parse_exception(d.pop("exception", UNSET))

        def _parse_exception_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        exception_type = _parse_exception_type(d.pop("exceptionType", UNSET))

        def _parse_level(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        level = _parse_level(d.pop("level", UNSET))

        def _parse_logger(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        logger = _parse_logger(d.pop("logger", UNSET))

        def _parse_message(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        message = _parse_message(d.pop("message", UNSET))

        def _parse_method(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        method = _parse_method(d.pop("method", UNSET))

        log_resource = cls(
            id=id,
            time=time,
            exception=exception,
            exception_type=exception_type,
            level=level,
            logger=logger,
            message=message,
            method=method,
        )

        return log_resource
