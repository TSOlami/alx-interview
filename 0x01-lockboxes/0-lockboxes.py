#!/usr/bin/python3
""" Can unlock all boxes"""


def canUnlockAll(boxes):
    # Check if the input is a list of boxes
    if not isinstance(boxes, list):
        return False

    # Initialize a list to keep track of checked boxes
    checked = [False] * len(boxes)
    checked[0] = True

    stack = [0]
    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if 0 <= key < len(boxes) and not checked[key]:
                checked[key] = True
                stack.append(key)

    return all(checked)
