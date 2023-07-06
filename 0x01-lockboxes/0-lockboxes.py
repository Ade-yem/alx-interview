#!/usr/bin/python3
"""Lockboxes"""


def canUnlockAll(boxes):
    """determines if all the boxes can be opened."""
    opened_boxes = [False] * len(boxes)
    opened_boxes[0] = True
    for num in range(1, len(boxes)):
        for j in range(0, num):
            box = boxes[j]
            if num in box:
                opened_boxes[num] = True
            elif (num < len(boxes) - 2 and num in boxes[num + 1]):
                opened_boxes[num] = True
    return all(opened_boxes)
