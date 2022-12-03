#!/bin/python

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

lines = open("input", "r").read().splitlines()
res = 0
for line in lines:
    a = list(line)
    mid = round(len(a)/2)
    res += sum(list(map(charToPriority, getCommons(a[:mid], a[mid:]))))
print(res)
