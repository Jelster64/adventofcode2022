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
    return [arr[i:i+size] for i in range(0, len(arr), size)]

lines = open("input", "r").read().splitlines()
res1, res2 = 0, 0

for line in lines:
    a = list(line)
    mid = round(len(a)/2)
    res1 += sum(map(charToPriority, getCommons(a[:mid], a[mid:])))

for group in toGroups(lines, 3):
    # convert list of strings to list of char lists
    group = list(map(list, group))
    res2 += sum(map(charToPriority, reduce(getCommons, group)))

print(res1, res2)
