#!/usr/bin/python3
def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.

    Args:
        boxes (list of list of int): 
        A list of boxes, where each box is represented
        by a list of keys it contains. Each key is an
        integer representing a box that can be unlocked.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.


    """
    # Start with the first box (box 0) unlocked
    unlocked = set([0])
    
    # Use a stack to keep track of boxes to explore
    stack = [0]

    # Explore all reachable boxes
    while stack:
        current_box = stack.pop()
        # Iterate through keys in the current box
        for key in boxes[current_box]:
            # If the key unlocks a new box, add it to the unlocked set and stack
            if key not in unlocked and key < len(boxes):
                unlocked.add(key)
                stack.append(key)

    # Return True if all boxes are unlocked, otherwise False
    return len(unlocked) == len(boxes)

