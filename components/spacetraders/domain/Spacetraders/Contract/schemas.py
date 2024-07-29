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


class SpacetradersContractTermsPayment(BaseModel):
    onAccepted: int = Field(default=0)
    onFulfilled: int = Field(default=0)


class SpacetradersContractDeliverTerm(BaseModel):
    tradeSymbol: str = Field(default="")
    destinationSymbol: str = Field(default="")
    unitsRequired: int = Field(default=0)
    unitsFulfilled: int = Field(default=0)


class SpacetradersContractTerms(BaseModel):
    deadline: str = Field(default="")
    payment: SpacetradersContractTermsPayment = Field(default=None)
    deliver: list[SpacetradersContractDeliverTerm] = Field(default=None)
    accepted: bool = Field(default=False)
    fulfilled: bool = Field(default=False)
    expiration: str = Field(default="")
    deadlineToAccept: str = Field(default="")


class SpacetradersContractBase(BaseModel):
    id: str = Field(default="")
    factionSymbol: str = Field(default="")
    type: str = Field(default="")
    terms: SpacetradersContractTerms = Field(default=None)


class SpacetradersContract(SpacetradersContractBase):
    pass
