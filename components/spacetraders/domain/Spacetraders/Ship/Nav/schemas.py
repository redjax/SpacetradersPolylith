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


class SpacetradersNavLocation(BaseModel):
    symbol: str = Field(default="")
    type: str = Field(default="")
    systemSymbol: str = Field(default="")
    x: int = Field(default=0)
    y: int = Field(default=0)


class SpacetradersNavRoute(BaseModel):
    origin: SpacetradersNavLocation = Field(default=None)
    destination: SpacetradersNavLocation = Field(default=None)
    arrival: str = Field(default="")
    departureTime: str = Field(default="")


class SpacetradersShipNavBase(BaseModel):
    systemSymbol: str = Field(default="")
    waypointSymbol: str = Field(default="")
    route: SpacetradersNavRoute = Field(default=None)
    status: str = Field(default="")
    flightMode: str = Field(default="")


class SpacetradersShipNav(SpacetradersShipNavBase):
    pass
