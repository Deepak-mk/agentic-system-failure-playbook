from circuit_breaker import CircuitBreaker
from failure_budget import FailureBudget

breaker = CircuitBreaker(failure_threshold=3)
budget = FailureBudget(allowed_failures=2)

def execute_action(action):
    if breaker.is_open:
        print("[BLOCKED] Circuit breaker is open")
        return

    print(f"[EXECUTE] {action}")

    # Simulate repeated policy failures
    if action["risk"] == "high":
        print("[VIOLATION] High-risk action detected")

        breaker.record_failure()

        if not budget.consume():
            print("[ESCALATION] Manual review required")
            return

        print("[CONTAINMENT] Action paused")
    else:
        print("[SUCCESS] Action completed safely")