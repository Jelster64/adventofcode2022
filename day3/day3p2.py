#!/bin/python

def charToPriority(char: str) -> int:
    val = ord(char)
    if val <= 90:
        return val - 38
    return val - 96

def getCommons(one: list[str], two: list[str]) -> list[str]:
    res: set[str] = set()
    for x in one:
        for y in two:
            if x == y:
                res.add(x)
    return list(res)

def toGroups(arr: list[str], groupSize: int) -> list[list[str]]:
    res: list[list[str]] = []
    for i in range(0, len(arr), groupSize):
        res.append(arr[i:i+groupSize])
    return res

lines = open("input", "r").readlines()
res = 0
groups = toGroups(lines, 3)
for group in groups:
    # convert list of strings to list of char lists with trailing \n removed
    group = list(map(lambda x: list(x)[:-1], group))
    res += sum(list(map(charToPriority, getCommons(getCommons(group[0], group[1]), group[2]))))
print(res)
