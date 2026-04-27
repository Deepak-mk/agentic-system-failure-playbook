class CircuitBreaker:
    def __init__(self, failure_threshold=3):
        self.failure_threshold = failure_threshold
        self.failure_count = 0
        self.is_open = False

    def record_failure(self):
        self.failure_count += 1
        print(f"[FAILURE COUNT] {self.failure_count}")

        if self.failure_count >= self.failure_threshold:
            self.is_open = True
            print("[CIRCUIT BREAKER OPENED] Agent access blocked")

    def reset(self):
        self.failure_count = 0
        self.is_open = False
        print("[CIRCUIT BREAKER RESET]")