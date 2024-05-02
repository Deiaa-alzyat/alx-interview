#!/usr/bin/python3
"""
You have n number of locked boxes in front of you.
Each box is numbered sequentially
from 0 to n - 1 and each box may
contain keys to the other boxes.
"""
def canUnlockAll(boxes):
    # We start with the first box already unlocked
    unlocked = [0]  # A list to keep track of unlocked boxes
    keys = set(boxes[0])  # A set to keep track of all available keys
    queue = list(keys)  # A queue initialized with keys from the first box

    while queue:
        current_key = queue.pop(0)
        if current_key < len(boxes) and current_key not in unlocked:
            # If the key corresponds to a box and that box hasn't been unlocked
            unlocked.append(current_key)
            # Add new keys from the unlocked box to the queue
            for key in boxes[current_key]:
                if key not in keys:
                    queue.append(key)
                    keys.add(key)

    # If the number of unlocked boxes equals the number of total boxes, return True
    return len(unlocked) == len(boxes)
