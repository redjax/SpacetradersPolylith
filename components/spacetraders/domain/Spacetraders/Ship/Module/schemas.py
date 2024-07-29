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


class SpacetradersShipModuleRequirements(BaseModel):
    crew: int = Field(default=0)
    power: int = Field(default=0)
    slots: int = Field(default=0)


class SpacetradersShipModuleBase(BaseModel):
    symbol: str = Field(default="")
    name: str = Field(default="")
    description: str = Field(default="")
    capacity: int = Field(default="")
    requirements: SpacetradersShipModuleRequirements = Field(default=None)


class spacetradersShipModule(SpacetradersShipModuleBase):
    pass
