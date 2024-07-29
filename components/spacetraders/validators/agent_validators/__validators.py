import typing as t
import logging

log = logging.getLogger(__name__)

from spacetraders.domain.Spacetraders import Agent


def validate_agent_symbol(agent_symbol: str = None, trim_symbol: bool = False) -> str:
    if not agent_symbol:
        raise ValueError("Missing an agent symbol to validate")
    if not isinstance(agent_symbol, str):
        raise TypeError(
            f"agent_symbol should be a str. Got type: ({type(agent_symbol)})"
        )

    if len(agent_symbol) > 14:
        if not trim_symbol:
            raise ValueError(
                f"agent_symbol must be 14 characters or less. Symbol '{agent_symbol}' has {len(agent_symbol)} characters, and trim_symbol=False."
            )
        else:
            log.warning(
                f"agent_symbol '{agent_symbol}' has {len(agent_symbol)} characters. trim_symbol=True, trimming to 14 characters"
            )

            agent_symbol: str = Agent.trim_agent_symbol(agent_symbol=agent_symbol)
            log.debug(f"Trimmed agent symbol: {agent_symbol}")

    return agent_symbol
