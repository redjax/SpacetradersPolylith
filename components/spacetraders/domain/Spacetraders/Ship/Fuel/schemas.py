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


class SpacetradersShipFuelConsumed(BaseModel):
    amount: int = 0
    timestamp: str = Field(default="")


class SpacetradersShipFuelBase(BaseModel):
    current: int = Field(default=0)
    capacity: int = Field(default=0)
    consumed: SpacetradersShipFuelConsumed = Field(default=None)


class SpacetradersShipFuel(SpacetradersShipFuelBase):
    pass
