#!/bin/python
import copy
import operator
from functools import reduce

def printStructure(structure):
    print('\n'.join([''.join(s) for s in structure]))

# def visualizeRock(rock: list[tuple[int, int]]):
#     highestY = max(map(lambda r: r[0], rock))
#     s = [['.' for _ in range(7)] for _ in range(highestY+1)]
#     res, _ = addRockToChamber(rock, s)
#     printStructure(reversed(res[-4:]))

def translateW(rock: list[tuple[int, int]], direction: str) -> list[tuple[int, int]]:
    match direction:
        case '<':
            return translate(rock, 'left', 1)
        case '>':
            return translate(rock, 'right', 1)
        case 'V':
            return translate(rock, 'down', 1)
        case _:
            print("error")
            return [(0, 0)]

def translate(rock: list[tuple[int, int]], direction: str, steps: int) -> list[tuple[int, int]]:
    match direction:
        case 'left':
            return list(map(lambda r: (r[0], r[1] - steps), rock))
        case 'right':
            return list(map(lambda r: (r[0], r[1] + steps), rock))
        case 'down':
            return list(map(lambda r: (r[0] - steps, r[1]), rock))
        case 'up':
            return list(map(lambda r: (r[0] + steps, r[1]), rock))
    return rock

def collides(rock: list[tuple[int, int]], chamber: list[list[str]]) -> bool:
    return reduce(operator.or_, [x < 0 or x >= 7 or y < 0 or chamber[y][x] != '.' for y, x in rock])

def addRockToChamber(rock: list[tuple[int, int]], chamber: list[list[str]], highestRock: int) -> tuple[list[list[str]], int]:
    for y, x in rock:
        chamber[y][x] = '#'
    return chamber, max(list(map(lambda r: r[0], rock)) + [highestRock])

rockTypes = []

#   ..####.
rockTypes.append([(0, 2), (0, 3), (0, 4), (0, 5)])

#   ...#...
#   ..###..
#   ...#...
rockTypes.append([(2, 3), (1, 2), (1, 3), (1, 4), (0, 3)])

#   ....#..
#   ....#..
#   ..###..
rockTypes.append([(2, 4), (1, 4), (0, 2), (0, 3), (0, 4)])

#   ..#....
#   ..#....
#   ..#....
#   ..#....
rockTypes.append([(0, 2), (1, 2), (2, 2), (3, 2)])

#   ..##...
#   ..##...
rockTypes.append([(0, 2), (0, 3), (1, 2), (1, 3)])

def tetris(gasJets: list[str], chamberHeight: int, amountOfRocks: int):
    jetsOfHotGas = iter(gasJets)

    chamber = [['.' for _ in range(7)] for _ in range(chamberHeight)]
    highestRock = -1 # initially, this is the floor
    gasJet = True # flip flops between jet and fall

    for i in range(amountOfRocks):
        # spawn rock
        rock = copy.deepcopy(rockTypes[i % 5])
        rock = translate(rock, 'up', highestRock + 4)

        while True:
            direction = 'V'
            if gasJet:
                try:
                    direction = next(jetsOfHotGas)
                except:
                    jetsOfHotGas = iter(gasJets)
                    direction = next(jetsOfHotGas)
                gasJet = False
            else: # gravity
                gasJet = True
            newRock = translateW(rock, direction)

            if collides(newRock, chamber):
                if gasJet: # if this movement was caused by gravity
                    chamber, highestRock = addRockToChamber(rock, chamber, highestRock)
                    break # spawn a new rock
                else:
                    continue
            rock = newRock
    # printStructure(reversed(chamber[:20]))
    return highestRock + 1

with open('input', 'r') as f:
    jetsOfHotGas = list(f.read().strip('\n'))
print(tetris(jetsOfHotGas, 4000, 2022))
