#!/usr/bin/python3
"""Lockboxes"""


def canUnlockAll(boxes):
    num_boxes = len(boxes)
    unlocked = [False] * num_boxes
    unlocked[0] = True  # The first box is unlocked by default

    queue = [0]  # Start with the first box
    while queue:
        current_box = queue.pop(0)
        for key in boxes[current_box]:
            if key < num_boxes and not unlocked[key]:
                unlocked[key] = True
                queue.append(key)

    return all(unlocked)
