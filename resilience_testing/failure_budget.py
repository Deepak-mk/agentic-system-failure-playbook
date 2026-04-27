class FailureBudget:
    def __init__(self, allowed_failures=2):
        self.allowed_failures = allowed_failures
        self.current_failures = 0

    def consume(self):
        self.current_failures += 1

        if self.current_failures > self.allowed_failures:
            print("[FAILURE BUDGET EXCEEDED] Reduce autonomy level")
            return False

        return True