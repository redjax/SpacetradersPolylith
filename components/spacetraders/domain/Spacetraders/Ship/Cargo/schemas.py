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


class SpacetradersShipCargoBase(BaseModel):
    capacity: int = Field(default=0)
    units: int = Field(default=0)
    inventory: list = Field(default_factory=list)


class SpaceetradersShipCargo(SpacetradersShipCargoBase):
    pass
