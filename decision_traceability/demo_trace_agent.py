from trace_engine import DecisionTrace

def agent():
    trace = DecisionTrace()

    # Reasoning trace
    trace.add_reasoning("User requested refund")
    trace.add_reasoning("Customer is premium")
    trace.add_reasoning("Refund amount = 1000")

    # Tool trace
    trace.add_tool_call(
        tool_name="refund_api",
        input_data={"amount": 1000},
        output_data={"status": "success", "latency": "210ms"}
    )

    # Policy trace
    trace.set_policy_trace(
        version="v3.2",
        threshold="refund_limit=500",
        result="violation detected"
    )

    # Governance trace
    trace.set_governance_trace(
        owner="Finance Ops",
        escalation_path="manual review queue"
    )

    # Final action
    trace.set_final_action("rollback")

    trace.show()

if __name__ == "__main__":
    agent()