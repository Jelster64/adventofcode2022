#!/bin/python
# import copy
# import operator
from itertools import chain
import re

def countHashtags(char: str) -> bool:
    return char == '#'

with open('input', 'r') as f:
    pairs = list(map(lambda x: ((int(x[0]), int(x[1])), (int(x[2]), int(x[3]))), [re.findall(r'-?\d+', s) for s in f.read().splitlines()]))

lineToCheck = 2000000

res = {}

allPairs = list(chain(*pairs))
X = list(map(lambda x: x[0], allPairs))
Y = list(map(lambda x: x[1], allPairs))
highestX = max(X)
highestY = max(Y)
lowestX = min(X)
lowestY = min(Y)

for S, B in pairs:
   if B[1] == lineToCheck:
       res[B[0]] = 'B'
   if S[1] == lineToCheck:
       res[S[0]] = 'S'

for S, B in pairs:
    reach = abs(S[0] - B[0]) + abs(S[1] - B[1])
    if S[1] + reach >= lineToCheck \
            and S[1] - reach <= lineToCheck:
        yDistance = abs(S[1] - lineToCheck)
        width = (reach - yDistance) * 2 + 1
        leftBound = S[0] - (reach - yDistance)
        rightBound = S[0] + (reach - yDistance)
        for i in range(leftBound, rightBound+1):
            if i not in res:
                res[i] = '#'
        assert(width % 2 == 1)

print(sum(map(countHashtags, list(res.values()))))
