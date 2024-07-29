from __future__ import annotations

import logging

log = logging.getLogger(__name__)

from spacetraders.constants import DISABLE_LOGGER_NAMES
from spacetraders.domain import agent
from spacetraders.random_data import get_rand_agent_name
from spacetraders.register import build_register_agent_request
from spacetraders.register_api import print_api_url
from spacetraders.request_client import decoders, get_httpx_client

if __name__ == "__main__":
    logging.basicConfig(level="DEBUG")
    for _logger in DISABLE_LOGGER_NAMES:
        logging.getLogger(_logger).setLevel("WARNING")

    print_api_url()

    agent_symbol = get_rand_agent_name()
    log.debug(f"Registering agent '{agent_symbol}'")
    register_req = build_register_agent_request(agent_symbol=agent_symbol)

    with get_httpx_client() as client:
        res = client.send(register_req)
        log.debug(f"Register agent response: [{res.status_code}: {res.reason_phrase}]")

        if not res.status_code == 200:
            log.warning(f"Non-200 response text: {res.text}")

    _decoded = decoders.decode_response_content(res=res)
    _agent = agent.SpacetradersAgent(
        account_id=_decoded["data"]["agent"]["accountId"],
        symbol=_decoded["data"]["agent"]["symbol"],
        faction=_decoded["data"]["faction"]["symbol"],
        token=_decoded["data"]["token"],
    )
    log.debug(f"Registered agent: {_agent}")
