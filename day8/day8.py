#!/bin/python
import copy
from functools import reduce

def isTreeVisible(i: int, j: int) -> bool:
    if i == 0 or j == 0 or i == len(trees)-1 or j == len(trees[i])-1:
        return True
    height = trees[i][j]
    if max(trees[i][j+1:]) < height:
        return True
    if max(trees[i][:j]) < height:
        return True
    if max(map(lambda a: a[j], trees[i+1:])) < height:
        return True
    if max(map(lambda a: a[j], trees[:i])) < height:
        return True
    return False

def calculateScenicScore(i: int, j: int) -> int:
    height = trees[i][j]
    score = [0 for _ in range(4)]

    index = i - 1
    while index >= 0:
        score[0] += 1
        if trees[index][j] >= height:
            break
        index -= 1

    index = i + 1
    while index < len(trees[i]):
        score[1] += 1
        if trees[index][j] >= height:
            break
        index += 1

    index = j - 1
    while index >= 0:
        score[2] += 1
        if trees[i][index] >= height:
            break
        index -= 1

    index = j + 1
    while index < len(trees[i]):
        score[3] += 1
        if trees[i][index] >= height:
            break
        index += 1

    return reduce(lambda x, y: x * y, score)

with open("input", "r") as f:
    trees = list(map(lambda x: list(map(int, x)), (map(list, f.read().splitlines()))))
res = copy.deepcopy(trees)
scenic = copy.deepcopy(trees)

for i in range(len(trees)):
    for j in range(len(trees[i])):
        res[i][j] = isTreeVisible(i, j)
        scenic[i][j] = calculateScenicScore(i, j)

part1 = sum(map(lambda x: sum(list(map(int, x))), res))
part2 = max(map(max, scenic))

print(part1, part2)
