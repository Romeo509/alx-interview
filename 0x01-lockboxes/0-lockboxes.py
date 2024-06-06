#!/usr/bin/python3

def canUnlockAll(boxes):
    # Set to keep track of keys
    keys = set([0])  # Start with the keys in the first box

    # Queue to perform BFS
    queue = [0]  # Start with the first box

    while queue:
        current_box = queue.pop(0)  # Get the first box from the queue

        # Check each key in the current box
        for key in boxes[current_box]:
            # If the key opens a box that hasn't been visited yet
            if key not in keys and key < len(boxes):
                keys.add(key)  # Add the key to the set of keys
                queue.append(key)

        # Mark the current box as visited
        boxes[current_box] = []

    # If all boxes have been visited, return True
    return len(keys) == len(boxes)
