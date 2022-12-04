#!/bin/python
from functools import reduce

def charToPriority(char: str) -> int:
    val = ord(char)
    if val <= 90:
        return val - 38
    return val - 96

def getCommons(one: list[str], two: list[str]) -> list[str]:
    res = set()
    for x in one:
        for y in two:
            if x == y:
                res.add(x)
    return list(res)

def toGroups(arr: list[str], size: int) -> list[list[str]]:
    res = []
    for i in range(0, len(arr), size):
        res.append(arr[i:i+size])
    return res

lines = open("input", "r").read().splitlines()
res = 0
for group in toGroups(lines, 3):
    # convert list of strings to list of char lists
    group = list(map(lambda x: list(x), group))
    res += sum(map(charToPriority, reduce(getCommons, group)))
print(res)
