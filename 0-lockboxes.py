def canUnlockAll(boxes):
    unlocked = set([0])
    stack = [0]

    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if key not in unlocked and key < len(boxes):
                unlocked.add(key)
                stack.append(key)

    return len(unlocked) == len(boxes)
