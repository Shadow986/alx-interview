#!/usr/bin/python3

def canUnlockAll(boxes):
    """Determines if all boxes can be opened."""
    num_boxes = len(boxes)
    keys = set([0])

    while True:
        new_keys = set([key for key in keys for box in [boxes[key]] if box])
        if not new_keys or new_keys == keys:
            break
        keys = keys.union(new_keys)

    return num_boxes == len(keys)

# Test cases
boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # Expected output: True

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))  # Expected output: True

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))  # Expected output: False
