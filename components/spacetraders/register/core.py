from __future__ import annotations

import logging

log = logging.getLogger(__name__)

import json

import httpx
from spacetraders.constants import SPACETRADERS_API_BASE_URL

def build_register_agent_request(
    agent_symbol: str = None, agent_faction: str = "COSMIC"
) -> httpx.Request:
    agent_faction: str = agent_faction.upper()
    register_url: str = f"{SPACETRADERS_API_BASE_URL}/register"
    register_data = json.dumps({"symbol": agent_symbol, "faction": agent_faction})

    req: httpx.Request = httpx.Request(
        method="POST",
        url=register_url,
        headers={"content-type": "application/json"},
        data=register_data,
    )

    return req
