#!/usr/bin/python3
"""Determines if all the boxes can be opened"""


def canUnlockAll(boxes):
    """Returns True if all boxes can be opened, else False"""
    # A list to track visited boxes
    is_visited = [False] * len(boxes)
    is_visited[0] = True

    # A list to store available keys
    available_keys = [0]

    while not all(is_visited) and available_keys:
        # Get a key from the list
        current_key = available_keys.pop()
        current_box = boxes[current_key]

        # Explore keys in the current box
        for new_key in current_box:
            if 0 <= new_key < len(boxes) and not is_visited[new_key]:
                is_visited[new_key] = True
                available_keys.append(new_key)

    return all(is_visited)
