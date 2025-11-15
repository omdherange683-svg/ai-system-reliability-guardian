from adk import Agent, AgentWorkflow, ParallelWorkflow, SequentialWorkflow
from adk.builtins import FileTool
from adk.memory import InMemorySessionService

session = InMemorySessionService()

# ---------- Tools ----------
class LogReaderTool(FileTool):
    def read_logs(self, filepath: str):
        with open(filepath, 'r') as f:
            return f.read()

log_tool = LogReaderTool()

# ---------- Agents ----------
log_monitor_agent = Agent(
    name="log_monitor",
    instructions="""
    You are a log monitoring agent.
    Analyze logs, find anomalies, spikes, repeated failures, and suspicious patterns.
    Return a structured JSON with:
    - errors
    - warnings
    - anomalies
    """,
    tools=[log_tool]
)

outage_predict_agent = Agent(
    name="outage_predictor",
    instructions="""
    Based on detected anomalies, predict:
    - Likely outage risk (low/medium/high)
    - Possible components that can fail
    - Estimated time to failure
    """,
)

auto_fixer_agent = Agent(
    name="auto_remediator",
    instructions="""
    Recommend fixes based on predicted outage.
    Output:
    - immediate fix
    - long-term fix
    - commands or steps to follow
    """,
)

rca_agent = Agent(
    name="rca_generator",
    instructions="""
    Generate a full RCA report in Markdown:
    - Incident Summary
    - Root Cause
    - Timeline
    - Impact
    - Resolution
    - Preventive Measures
    """,
)

supervisor = Agent(
    name="supervisor",
    instructions="""
    You supervise all agents. Combine their outputs into a final
    System Reliability Report.
    """
)

# ---------- Workflow ----------
workflow = SequentialWorkflow(
    steps=[
        ParallelWorkflow(agents=[log_monitor_agent]),
        ParallelWorkflow(agents=[outage_predict_agent]),
        ParallelWorkflow(agents=[auto_fixer_agent]),
        ParallelWorkflow(agents=[rca_agent]),
        supervisor
    ]
)

# ---------- Runner ----------
def run_reliability_guardian(log_path):
    return workflow.run(
        {"filepath": log_path},
        session=session
    )

if __name__ == "__main__":
    result = run_reliability_guardian("sample_logs.txt")
    print(result)
