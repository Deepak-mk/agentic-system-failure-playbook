from datetime import datetime

class ActionJournal:
    def __init__(self):
        self.log = []
        self.state = {
            "balance": 5000,
            "transactions": []
        }

    def record(self, action):
        entry = {
            "action": action,
            "timestamp": datetime.now().isoformat(),
            "status": "executed"
        }
        self.log.append(entry)

    def mark_reversed(self, action):
        for entry in self.log:
            if entry["action"] == action:
                entry["status"] = "reversed"