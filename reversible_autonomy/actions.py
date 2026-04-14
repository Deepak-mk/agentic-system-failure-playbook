def execute_action(action, journal):
    print(f"[EXECUTE] {action}")

    # Record action
    journal.record(action)

    # Simulate state mutation
    if action["type"] == "refund":
        journal.state["balance"] -= action["amount"]
        journal.state["transactions"].append(action)


def rollback_action(action, journal):
    print(f"[ROLLBACK] {action}")

    # Reverse state change
    if action["type"] == "refund":
        journal.state["balance"] += action["amount"]
        journal.state["transactions"].remove(action)

    journal.mark_reversed(action)