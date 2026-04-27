from demo_resilience_agent import execute_action

def run():
    risky_action = {"type": "payment", "risk": "high"}

    print("\n--- RESILIENCE TEST ---")

    for _ in range(4):
        execute_action(risky_action)

if __name__ == "__main__":
    run()