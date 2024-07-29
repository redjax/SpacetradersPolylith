from __future__ import annotations

import logging
import json

log = logging.getLogger(__name__)

from spacetraders.constants import SPACETRADERS_API_BASE_URL
from spacetraders import request_client, registration
from spacetraders.domain.Spacetraders import Agent, Contract, Faction
from spacetraders.DTO import SpacetradersDTO
from spacetraders.validators import agent_validators

import httpx


def print_api_url() -> None:
    print(f"API base URL: {SPACETRADERS_API_BASE_URL}")


def handle_request(req: httpx.Request = None) -> httpx.Response:
    with request_client.get_httpx_client(
        headers={"content-type": "application/json"}
    ) as client:
        try:
            res: httpx.Response = client.send(request=req)

            return res
        except Exception as exc:
            msg = f"({type(exc)}) Unhandled exception registering agent. Details: {exc}"
            log.error(msg)

            raise exc


def parse_register_agent_response(
    res: httpx.Response = None,
) -> SpacetradersDTO.RegisteredAgentDTO:
    _decoded = request_client.decoders.decode_response_content(res=res)["data"]
    # log.debug(f"Decoded register agent response: {_decoded}")

    register_agent_res: SpacetradersDTO.RegisteredAgentDTO = (
        SpacetradersDTO.RegisteredAgentDTO.model_validate(_decoded)
    )

    return register_agent_res


def register_new_agent(agent_symbol: str = None, agent_faction: str = "COSMIC"):
    agent_symbol = agent_validators.validate_agent_symbol(
        agent_symbol=agent_symbol, trim_symbol=True
    )

    register_agent_req: httpx.Request = registration.build_register_agent_request(
        agent_symbol=agent_symbol, agent_faction=agent_faction.upper()
    )

    res: httpx.Response = handle_request(req=register_agent_req)

    log.debug(f"Register agent response: [{res.status_code}: {res.reason_phrase}]")
    if not res.status_code in [200, 201]:
        log.warning(f"Non-200 response: [{res.status_code}] {res.text}")

        return None

    else:
        registered_agent_dto: SpacetradersDTO.RegisteredAgentDTO = (
            parse_register_agent_response(res=res)
        )
        # log.debug(f"Register agent API response: {register_agent_res}")

        # registered_agent: Agent.SpacetradersAgent = (
        #     Agent.SpacetradersAgent.model_validate(register_agent_res.agent)
        # )

        log.debug(
            f"Registered Agent ({type(registered_agent_dto)}): {registered_agent_dto}"
        )
