#!/usr/bin/python3
"""
0-lockboxes.py
"""
def canUnlockAll(boxes):
    """
	Determines if all the boxes can be opened.
    Args:
        boxes: List of list
    Returns:
        True or false
    """
    unlocked = set([0])
    stack = [0]

    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if key not in unlocked and key < len(boxes):
                unlocked.add(key)
                stack.append(key)

    return len(unlocked) == len(boxes)
