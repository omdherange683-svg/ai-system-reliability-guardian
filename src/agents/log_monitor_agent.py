from adk import Agent

log_monitor_agent = Agent(
    name="log_monitor",
    instructions="""
    You are a log monitoring agent.
    Analyze logs, find anomalies, spikes, repeated failures, and suspicious patterns.
    Return structured JSON:
    - errors
    - warnings
    - anomalies
    """
)
