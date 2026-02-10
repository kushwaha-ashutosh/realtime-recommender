import json
import random
import time
import uuid
from datetime import datetime

EVENT_FILE = "events.jsonl"

NUM_USERS = 100
NUM_ITEMS = 50


def generate_event():
    return {
        "event_id": str(uuid.uuid4()),
        "user_id": random.randint(0, NUM_USERS - 1),
        "item_id": random.randint(0, NUM_ITEMS - 1),
        "event_type": "click",
        "timestamp": datetime.utcnow().isoformat()
    }


def main():
    print("Starting event producer...")

    with open(EVENT_FILE, "a") as f:
        while True:
            event = generate_event()
            f.write(json.dumps(event) + "\n")
            f.flush()

            print("Produced:", event)
            time.sleep(0.5)


if __name__ == "__main__":
    main()
