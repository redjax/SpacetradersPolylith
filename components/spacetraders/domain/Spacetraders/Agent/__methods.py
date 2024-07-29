def trim_agent_symbol(agent_symbol: str = None) -> str:
    if not isinstance(agent_symbol, str):
        agent_symbol: str = f"{agent_symbol}"

    agent_symbol: str = agent_symbol.replace("-", "")

    if len(agent_symbol) > 14:
        agent_symbol = agent_symbol[:14]

    return agent_symbol
