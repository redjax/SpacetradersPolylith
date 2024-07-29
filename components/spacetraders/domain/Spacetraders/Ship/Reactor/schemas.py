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


class SpacetraderShipRequirements(BaseModel):
    crew: int = Field(default=0)


class SpacetraderShipReactorBase(BaseModel):
    symbol: str = Field(default="")
    name: str = Field(default="")
    description: str = Field(default="")
    condition: int = Field(default=0)
    integrity: int = Field(default=0)
    powerOutput: int = Field(default=0)


class SpacetraderShipReactor(SpacetraderShipReactorBase):
    pass
