from adk import Agent

outage_predict_agent = Agent(
    name="outage_predictor",
    instructions="""
    Based on detected anomalies, predict:
    - Likely outage risk (low/medium/high)
    - Components that may fail
    - Estimated time to failure
    """
)
