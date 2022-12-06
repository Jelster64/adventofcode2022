#!/bin/python

def firstMarker(chars: str, length: int) -> int:
    for i in range(len(chars)):
        if len(set(chars[i:i+length])) == length:
            return i + length
    return -1

chars = open("input", "r").read()
part1 = firstMarker(chars, 4)
part2 = firstMarker(chars, 14)
print(part1, part2)
