import typing as t
import logging

log = logging.getLogger(__name__)

from pydantic import (
    BaseModel,
    Field,
    field_validator,
    ValidationError,
    computed_field,
    ConfigDict,
)


class SpacetradersShipCrewBase(BaseModel):
    current: int = Field(default=0)
    capacity: int = Field(default=0)
    required: int = Field(default=0)
    rotation: str = Field(default="")
    morale: int = Field(default=0)
    wages: int = Field(default=0)


class SpacetradersShipCrew(SpacetradersShipCrewBase):
    pass
