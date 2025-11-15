from adk import Agent

auto_fixer_agent = Agent(
    name="auto_remediator",
    instructions="""
    Recommend fixes based on predicted outage.
    Output:
    - immediate fix
    - long-term fix
    - commands or steps
    """
)
