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
    pass


class SpacetradersAgent(SpacetradersAgentBase):
    account_id: str = Field(default=None)
    symbol: str = Field(default=None)
    faction: str = Field(default=None)
    token: str = Field(default=None, repr=False)
