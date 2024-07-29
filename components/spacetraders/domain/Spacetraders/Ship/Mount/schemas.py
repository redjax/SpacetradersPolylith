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


class SpacetradersShipMountRequirement(BaseModel):
    crew: int = Field(default=0)
    power: int = Field(default=0)


class SpacetradersShipMountBase(BaseModel):
    symbol: str = Field(default="")
    name: str = Field(default="")
    description: str = Field(default="")
    strength: int = Field(default=0)
    requirements: SpacetradersShipMountRequirement = Field(default=None)
    deposits: list[str] | None = Field(default_factory=list)


class SpacetradersShipMount(SpacetradersShipMountBase):
    pass
