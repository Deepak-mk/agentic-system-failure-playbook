from demo_reversible_agent import agent

def run():
    safe_action = {"type": "refund", "amount": 200}
    risky_action = {"type": "refund", "amount": 1000}

    print("\n--- SAFE ACTION ---")
    agent(safe_action)

    print("\n--- RISKY ACTION ---")
    agent(risky_action)

if __name__ == "__main__":
    run()