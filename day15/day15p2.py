#!/bin/python
import re

lowestX = 0
lowestY = 0
highestX = 4000000
highestY = 4000000

def inBounds(point: tuple[int, int]) -> bool:
    return lowestX <= point[0] <= highestX and lowestY <= point[1] <= highestY

def getDistance(S: tuple[int, int], B: tuple[int, int]) -> int:
    return abs(S[0] - B[0]) + abs(S[1] - B[1])

def calculateResult(point: tuple[int, int]) -> int:
    return point[0] * 4000000 + point[1]

def isOutsideOfRange(p: tuple[int, int], pairs: list[tuple[tuple[int, int], tuple[int, int]]]) -> bool:
    for S, B in pairs:
        if getDistance(S, p) <= getDistance(S, B):
            return False
    return True

def findBeacon(pairs: list[tuple[tuple[int, int], tuple[int, int]]]) -> int:
    alreadyChecked = set()
    for S, B in pairs:
        distance = getDistance(S, B) + 1
        for i in range(distance + 1):
            j = distance - i
            points = ((S[0] + i, S[1] + j),\
                      (S[0] + i, S[1] - j),\
                      (S[0] - i, S[1] + j),\
                      (S[0] - i, S[1] - j))
            for p in points:
                if inBounds(p) and p not in alreadyChecked:
                    if isOutsideOfRange(p, pairs):
                        return calculateResult(p)
                    else:
                        alreadyChecked.add(p)
    return -1

with open('input', 'r') as f:
    pairs = list(map(lambda x: ((int(x[0]), int(x[1])), (int(x[2]), int(x[3]))), [re.findall(r'-?\d+', s) for s in f.read().splitlines()]))
print(findBeacon(pairs))
