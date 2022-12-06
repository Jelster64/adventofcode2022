#!/bin/python
from collections import deque

def firstMarker(chars: list[str], length: int) -> int:
    queue = deque()
    for i, c in zip(range(len(chars)), chars):
        queue.append(c)
        if len(set(queue)) == length:
            return i+1
        if len(queue) >= length:
            queue.popleft()
    return -1

chars = list(open("input", "r").read())
part1 = firstMarker(chars, 4)
part2 = firstMarker(chars, 14)
print(part1, part2)
