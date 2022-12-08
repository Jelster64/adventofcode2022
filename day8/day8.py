#!/bin/python
import copy
from functools import reduce

def isTreeVisible(i: int, j: int, trees: list[list[int]]) -> bool:
    if i == 0 or j == 0 \
        or i == len(trees)-1 \
        or j == len(trees[i])-1:
        return True
    height = trees[i][j]
    return max(trees[i][j+1:]) < height \
        or max(trees[i][:j]) < height \
        or max(map(lambda a: a[j], trees[i+1:])) < height \
        or max(map(lambda a: a[j], trees[:i])) < height

def lineOfSightScore(lineOfSight: list[int], height: int) -> int:
    score = 0
    for tree in lineOfSight:
        score += 1
        if tree >= height:
            return score
    return score

def scenicScore(i: int, j: int, trees: list[list[int]]) -> int:
    height = trees[i][j]
    linesOfSight = [list(reversed(trees[i][:j])),\
                    trees[i][j+1:],\
                    list(reversed([trees[k][j] for k in range(i)])),\
                    [trees[k][j] for k in range(i+1, len(trees[i]))]]
    return reduce(lambda x, y: x * y, map(lambda x: lineOfSightScore(x, height), linesOfSight))

with open("input", "r") as f:
    trees = list(map(lambda row: list(map(int, row)), f.read().splitlines()))
visible = copy.deepcopy(trees)
scenic = copy.deepcopy(trees)

for i in range(len(trees)):
    for j in range(len(trees[i])):
        visible[i][j] = isTreeVisible(i, j, trees)
        scenic[i][j] = scenicScore(i, j, trees)

part1 = sum(map(lambda x: sum(list(map(int, x))), visible))
part2 = max(map(max, scenic))
print(part1, part2)
