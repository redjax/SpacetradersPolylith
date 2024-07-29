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


class SpacetradersShipRegistrationBase(BaseModel):
    name: str = Field(default="")
    factionSymbol: str = Field(default="")
    role: str = Field(default="")


class SpacetradersShipRegistration(SpacetradersShipRegistrationBase):
    pass
