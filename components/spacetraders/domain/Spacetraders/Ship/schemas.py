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

from . import Crew, Nav, Fuel, Frame, Reactor, Module, Mount, Registration, Cargo


class SpacetraderShipCooldown(BaseModel):
    shipSymbol: str = Field(default="")
    totalSeconds: int = Field(default=0)
    remainingSeconds: int = Field(default=0)


class SpacetradersShipBase(BaseModel):
    symbol: str = Field(default="")
    nav: Nav.SpacetradersShipNav = Field(default=None)
    crew: Crew.SpacetradersShipCrew = Field(default=None)
    fuel: Fuel.SpacetradersShipFuel = Field(default=None)
    cooldown: SpacetraderShipCooldown = Field(default=None)
    frame: Frame.SpacetradersShipFrame = Field(default=None)
    reactor: Reactor.SpacetraderShipReactor = Field(defult=None)
    modules: list[Module.spacetradersShipModule] = Field(default=None)
    mounts: list[Mount.SpacetradersShipMount] = Field(default=None)
    registration: Registration.SpacetradersShipRegistration = Field(default=None)
    cargo: Cargo.SpaceetradersShipCargo = Field(default=None)


class SpacetradersShip(SpacetradersShipBase):
    pass
