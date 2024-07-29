from __future__ import annotations

import logging

log = logging.getLogger(__name__)
import uuid

def trim_agent_symbol(agent_symbol: str = None) -> str:
    if not isinstance(agent_symbol, str):
        agent_symbol: str = f"{agent_symbol}"

    agent_symbol = agent_symbol.replace("-", "")

    if len(agent_symbol) > 14:
        agent_symbol = agent_symbol[:14]

    return agent_symbol


def get_rand_agent_name() -> str:
    agent_uuid_str: uuid.UUID = uuid.uuid4()
    trimmed_symbol: str = trim_agent_symbol(agent_symbol=f"{agent_uuid_str}")

    return trimmed_symbol
