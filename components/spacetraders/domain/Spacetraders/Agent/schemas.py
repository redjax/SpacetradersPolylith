from __future__ import annotations

import logging

log = logging.getLogger(__name__)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    ValidationError,
    computed_field,
    field_validator,
)


class SpacetradersAgentBase(BaseModel):
    accountId: str = Field(default="")
    symbol: str = Field(default="")
    headquarters: str = Field(default="")
    credits: int = Field(default=0)
    startingFaction: str = Field(default="")
    shipCount: int = Field(default=0)


class SpacetradersAgent(SpacetradersAgentBase):
    pass
