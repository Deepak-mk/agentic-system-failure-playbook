def policy_check(action):
    # Example rule: refunds > 500 require approval
    if action["type"] == "refund" and action["amount"] > 500:
        return {
            "allowed": False,
            "reason": "Refund exceeds approval limit"
        }

    return {"allowed": True}