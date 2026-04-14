from journal import ActionJournal
from policy_engine import policy_check
from actions import execute_action, rollback_action

journal = ActionJournal()

def agent(action):
    print(f"\n[AGENT RECEIVED] {action}")

    # Step 1: Execute action
    execute_action(action, journal)

    # Step 2: Validate via policy
    decision = policy_check(action)

    if not decision["allowed"]:
        print(f"[VIOLATION] {decision['reason']}")

        # Step 3: Rollback
        rollback_action(action, journal)
    else:
        print("[APPROVED] Action within policy")

    print(f"[FINAL STATE] {journal.state}")