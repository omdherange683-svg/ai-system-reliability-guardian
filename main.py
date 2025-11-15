from workflows.reliability_workflow import run_reliability_guardian

if __name__ == "__main__":
    result = run_reliability_guardian("utils/sample_logs.txt")
    print(result)
