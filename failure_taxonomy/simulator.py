from demo_agent import agent

def run_scenarios():
    print("\n--- Scenario 1: Safe ---")
    agent("check status")

    print("\n--- Scenario 2: Risky ---")
    agent("process refund for premium customer")

if __name__ == "__main__":
    run_scenarios()