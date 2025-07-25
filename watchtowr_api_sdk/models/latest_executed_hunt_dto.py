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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List
from watchtowr_api_sdk.models.hunt_acknowledgement_dto import HuntAcknowledgementDto
from watchtowr_api_sdk.models.threat_actor_dto import ThreatActorDto
from typing import Optional, Set
from typing_extensions import Self

class LatestExecutedHuntDto(BaseModel):
    """
    LatestExecutedHuntDto
    """ # noqa: E501
    id: StrictStr = Field(description="Hunt identifier")
    title: StrictStr = Field(description="Hunt title")
    status: StrictStr = Field(description="Hunt status")
    total_findings: StrictFloat = Field(description="Number of findings discovered", alias="totalFindings")
    total_assets: StrictFloat = Field(description="Number of assets affected", alias="totalAssets")
    need_investigation: StrictBool = Field(description="Whether manual investigation is required", alias="needInvestigation")
    request_type: StrictStr = Field(description="Type of hunt request", alias="requestType")
    resolved_status: StrictBool = Field(description="Whether the hunt has been resolved", alias="resolvedStatus")
    acknowledgement: HuntAcknowledgementDto = Field(description="Hunt acknowledgement data")
    threat_actors: List[ThreatActorDto] = Field(description="Associated threat actors", alias="threatActors")
    __properties: ClassVar[List[str]] = ["id", "title", "status", "totalFindings", "totalAssets", "needInvestigation", "requestType", "resolvedStatus", "acknowledgement", "threatActors"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['in-progress', 'completed']):
            raise ValueError("must be one of enum values ('in-progress', 'completed')")
        return value

    @field_validator('request_type')
    def request_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['Misconfig', 'Others', 'SoftwareVulnerability', 'ThreatIntelligence']):
            raise ValueError("must be one of enum values ('Misconfig', 'Others', 'SoftwareVulnerability', 'ThreatIntelligence')")
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
        """Create an instance of LatestExecutedHuntDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of acknowledgement
        if self.acknowledgement:
            _dict['acknowledgement'] = self.acknowledgement.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in threat_actors (list)
        _items = []
        if self.threat_actors:
            for _item_threat_actors in self.threat_actors:
                if _item_threat_actors:
                    _items.append(_item_threat_actors.to_dict())
            _dict['threatActors'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of LatestExecutedHuntDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in LatestExecutedHuntDto) in the input: " + _key)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "title": obj.get("title"),
            "status": obj.get("status"),
            "totalFindings": obj.get("totalFindings"),
            "totalAssets": obj.get("totalAssets"),
            "needInvestigation": obj.get("needInvestigation"),
            "requestType": obj.get("requestType"),
            "resolvedStatus": obj.get("resolvedStatus"),
            "acknowledgement": HuntAcknowledgementDto.from_dict(obj["acknowledgement"]) if obj.get("acknowledgement") is not None else None,
            "threatActors": [ThreatActorDto.from_dict(_item) for _item in obj["threatActors"]] if obj.get("threatActors") is not None else None
        })
        return _obj


