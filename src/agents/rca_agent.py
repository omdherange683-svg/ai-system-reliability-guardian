from adk import Agent

rca_agent = Agent(
    name="rca_generator",
    instructions="""
    Create RCA report in Markdown:
    - Summary
    - Root Cause
    - Timeline
    - Impact
    - Resolution
    - Prevention
    """
)
