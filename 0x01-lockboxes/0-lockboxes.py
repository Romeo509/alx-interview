#!/usr/bin/python3
"""
This module contains the canUnlockAll function.
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Parameters:
    boxes (list of list of int): A list of
    boxes where each box contains a list of keys.

    Returns:
    bool: True if all boxes can be opened, False otherwise.
    """
    keys = set([0])
    queue = [0]

    while queue:
        current_box = queue.pop(0)

        for key in boxes[current_box]:
            if key not in keys and key < len(boxes):
                keys.add(key)
                queue.append(key)

        boxes[current_box] = []

    return len(keys) == len(boxes)
