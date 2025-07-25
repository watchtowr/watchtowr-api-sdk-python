# coding: utf-8

"""
    Complete watchTowr Platform API Documentation

    The watchTowr Client API combining all watchTowr Platform APIs into a single comprehensive reference, including:       * Continuous Assurance API       * Adversary Sight API       * Intelligence API       * Platform API 

    The version of the OpenAPI document: 1.0
    Contact: support@watchTowr.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List
from typing import Optional, Set
from typing_extensions import Self

class FindingRetestResponseDto(BaseModel):
    """
    FindingRetestResponseDto
    """ # noqa: E501
    requested_by: StrictStr
    requested_at: datetime
    retest_status: StrictStr
    status_occurred_at: datetime
    completed_at: datetime
    evidence: StrictStr
    __properties: ClassVar[List[str]] = ["requested_by", "requested_at", "retest_status", "status_occurred_at", "completed_at", "evidence"]

    @field_validator('retest_status')
    def retest_status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['started', 'in-progress', 'success', 'error']):
            raise ValueError("must be one of enum values ('started', 'in-progress', 'success', 'error')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of FindingRetestResponseDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FindingRetestResponseDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in FindingRetestResponseDto) in the input: " + _key)

        _obj = cls.model_validate({
            "requested_by": obj.get("requested_by"),
            "requested_at": obj.get("requested_at"),
            "retest_status": obj.get("retest_status"),
            "status_occurred_at": obj.get("status_occurred_at"),
            "completed_at": obj.get("completed_at"),
            "evidence": obj.get("evidence")
        })
        return _obj


