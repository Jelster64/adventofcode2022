#!/bin/python
import copy
import operator
from itertools import chain

with open('input', 'r') as f:
    rockvectors = list(map(lambda x: x.split('->'), f.read().splitlines()))
rockvectors = list(map(lambda x: list(map(lambda y: list(map(int, y.split(','))), x)), rockvectors))

def getRockStructure(rockvectors) -> list[list[str]]:
    highestY = max(map(lambda x: x[1], list(chain(*rockvectors))))
    structure = [['.' for _ in range(highestY+1)] for _ in range(700)]
    for sequence in rockvectors:
        previous = None
        for r in sequence:
            if previous == None:
                structure[r[0]][r[1]] = '#'
                previous = r
                continue
            x, y = previous[0], previous[1]
            if x == r[0]:
                op = operator.add if y < r[1] else operator.sub
                while y != r[1]:
                    structure[x][y] = '#'
                    y = op(y, 1)
            if y == r[1]:
                op = operator.add if x < r[0] else operator.sub
                while x != r[0]:
                    structure[x][y] = '#'
                    x = op(x, 1)
            structure[x][y] = '#'
            previous = r
    return structure

def dropSand(structure) -> bool:
    x, y = 500, -1
    if structure[x][y+1] != '.':
        return False
    while y < len(structure[0])-1:
        y += 1
        if structure[x][y] == '.':
            continue
        elif structure[x-1][y] == '.':
            x -= 1
        elif structure[x+1][y] == '.':
            x += 1
        else:
            structure[x][y-1] = 'o'
            return True
    return False

def printStructure(structure):
    print('\n'.join([''.join(s) for s in structure]))

def partone(structure) -> int:
    res = 0
    while dropSand(structure):
        res += 1
    return res

def parttwo(structure) -> int:
    res = 0
    for row in structure:
        row += ['.', '#']
    while dropSand(structure):
        res += 1
    return res

s1 = getRockStructure(rockvectors)
s2 = copy.deepcopy(s1)
part1, part2 = partone(s1), parttwo(s2)
# printStructure(s2)
print(part1, part2)
