#!/usr/bin/python3
"""  Module for lockboxes  """


def canUnlockAll(boxes):
    """Determines if all boxes can be opened using the keys provided."""

    n = len(boxes)
    opened = [False] * n
    opened[0] = True

    queue = [0]

    while queue:
        current_box = queue.pop(0)
        for key in boxes[current_box]:
            if key < n and not opened[key]:
                opened[key] = True
                queue.append(key)

    return all(opened)
