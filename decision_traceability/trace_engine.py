from datetime import datetime

class DecisionTrace:
    def __init__(self):
        self.trace = {
            "timestamp": datetime.now().isoformat(),
            "reasoning_trace": [],
            "tool_trace": [],
            "policy_trace": {},
            "governance_trace": {},
            "final_action": None
        }

    def add_reasoning(self, step):
        self.trace["reasoning_trace"].append(step)

    def add_tool_call(self, tool_name, input_data, output_data):
        self.trace["tool_trace"].append({
            "tool": tool_name,
            "input": input_data,
            "output": output_data
        })

    def set_policy_trace(self, version, threshold, result):
        self.trace["policy_trace"] = {
            "policy_version": version,
            "threshold": threshold,
            "result": result
        }

    def set_governance_trace(self, owner, escalation_path):
        self.trace["governance_trace"] = {
            "owner": owner,
            "escalation_path": escalation_path
        }

    def set_final_action(self, action):
        self.trace["final_action"] = action

    def show(self):
        print("\n=== DECISION TRACE ===")
        for key, value in self.trace.items():
            print(f"{key}: {value}")