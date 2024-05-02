#!/usr/bin/python3
"""
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1
and each box may contain keys to the other boxes.
"""

def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.
    
    Args:
        boxes (list of list of int): The list of boxes, where each box contains keys to other boxes.
    
    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    unlocked = set([0])  # Set to track unlocked boxes
    keys = [0]  # Start with keys from box 0

    while keys:
        new_keys = []
        for key in keys:
            for new_key in boxes[key]:
                if new_key not in unlocked and new_key < len(boxes):
                    unlocked.add(new_key)
                    new_keys.append(new_key)
        keys = new_keys  # Update keys with new keys found

    return len(unlocked) == len(boxes)
