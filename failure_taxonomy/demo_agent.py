from policy_engine import policy_check

def planner(user_input):
    # Simulate reasoning (intentionally flawed)
    if "refund" in user_input:
        return {"action": "process_refund", "amount": 1000}
    return {"action": "noop"}

def execute(plan):
    print(f"[EXECUTE] Executing action: {plan}")
    return "done"

def agent(user_input):
    print(f"\n[INPUT] {user_input}")

    plan = planner(user_input)
    print(f"[PLAN] {plan}")

    decision = policy_check(plan)

    if decision["allowed"]:
        result = execute(plan)
    else:
        print(f"[BLOCKED] {decision['reason']}")
        result = "escalated"

    print(f"[RESULT] {result}")

if __name__ == "__main__":
    agent("process refund for premium customer")