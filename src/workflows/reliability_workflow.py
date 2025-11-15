from adk import SequentialWorkflow, ParallelWorkflow
from adk.memory import InMemorySessionService

from agents.log_monitor_agent import log_monitor_agent
from agents.outage_predict_agent import outage_predict_agent
from agents.auto_fixer_agent import auto_fixer_agent
from agents.rca_agent import rca_agent
from agents.supervisor_agent import supervisor
from tools.log_reader_tool import LogReaderTool

session = InMemorySessionService()
log_tool = LogReaderTool()

workflow = SequentialWorkflow(
    steps=[
        ParallelWorkflow(agents=[log_monitor_agent]),
        ParallelWorkflow(agents=[outage_predict_agent]),
        ParallelWorkflow(agents=[auto_fixer_agent]),
        ParallelWorkflow(agents=[rca_agent]),
        supervisor
    ]
)

def run_reliability_guardian(log_path):
    return workflow.run(
        {"filepath": log_path},
        session=session
    )
