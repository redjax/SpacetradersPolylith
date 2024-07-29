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


class SpacetradersShipFrameRequirements(BaseModel):
    power: int = Field(default=0)
    crew: int = Field(default=0)


class SpacetradersShipFrameBase(BaseModel):
    symbol: str = Field(default="")
    name: str = Field(default="")
    description: str = Field(default="")
    moduleSlots: int = Field(default=0)
    mountingPoints: int = Field(default=0)
    condition: int = Field(default=0)
    integrity: int = Field(default=0)
    requirements: SpacetradersShipFrameRequirements = Field(default=None)


class SpacetradersShipFrame(SpacetradersShipFrameBase):
    pass
