#!/bin/python
from collections import deque

def firstMarker(chars: list[str], length: int) -> int:
    marker = deque()
    for i, c in zip(range(len(chars)), chars):
        marker.append(c)
        if len(set(marker)) == length:
            return i+1
        if len(marker) >= length:
            marker.popleft()
    return -1

chars = list(open("input", "r").read())
part1 = firstMarker(chars, 4)
part2 = firstMarker(chars, 14)
print(part1, part2)
