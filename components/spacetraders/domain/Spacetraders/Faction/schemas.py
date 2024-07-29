import typing as t
import logging

log = logging.getLogger(__name__)

from pydantic import (
    BaseModel,
    Field,
    field_validator,
    ValidationError,
    ConfigDict,
    computed_field,
)


class SpacetradersFactionTrait(BaseModel):
    symbol: str = Field(default="")
    name: str = Field(default="")
    description: str = Field(default="")


class SpacetradersFactionBase(BaseModel):
    symbol: str = Field(default="")
    name: str = Field(default="")
    description: str = Field(default="")
    headquarters: str = Field(default="")
    traits: list[SpacetradersFactionTrait] = Field(default=None)
    isRecruiting: bool = Field(default=False)


class SpacetradersFaction(SpacetradersFactionBase):
    pass
