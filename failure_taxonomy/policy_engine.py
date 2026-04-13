def policy_check(plan):
    # Simple rule: block large refunds
    if plan.get("action") == "process_refund" and plan.get("amount", 0) > 500:
        return {
            "allowed": False,
            "reason": "Amount exceeds approval threshold"
        }

    return {"allowed": True}