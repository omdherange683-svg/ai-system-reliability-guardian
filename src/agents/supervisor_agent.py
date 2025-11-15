from adk import Agent

supervisor = Agent(
    name="supervisor",
    instructions="""
    You coordinate all agents and combine their outputs
    into a final System Reliability Report.
    """
)
