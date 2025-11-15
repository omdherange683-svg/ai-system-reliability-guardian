from adk.builtins import FileTool

class LogReaderTool(FileTool):
    def read_logs(self, filepath: str):
        with open(filepath, 'r') as f:
            return f.read()
