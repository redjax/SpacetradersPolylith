import typing as t
import logging

log = logging.getLogger(__name__)

from spacetraders.domain.Spacetraders import Agent, Faction, Contract, Ship

from pydantic import (
    BaseModel,
    Field,
    field_validator,
    ValidationError,
    ConfigDict,
    computed_field,
)


class RegisteredAgentDTOBase(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    token: str = Field(default=None, repr=False)
    agent: Agent.SpacetradersAgent = Field(default=None)
    contract: Contract.SpacetradersContract = Field(default=None)
    faction: Faction.SpacetradersFaction = Field(default=None)
    ship: Ship.SpacetradersShip = Field(default=None)


class RegisteredAgentDTO(RegisteredAgentDTOBase):
    pass
