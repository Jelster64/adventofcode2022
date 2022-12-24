#!/bin/python
import collections

Move = collections.namedtuple('Move', ['i', 'j', 'direction'])

def printStructure(structure):
    print('\n'.join([''.join(s) for s in structure]))

def surroundingNorth(grove: list[list[str]], i: int, j: int) -> bool:
    return grove[i-1][j-1] == '#'\
    or grove[i-1][j] == '#'\
    or grove[i-1][j+1] == '#'

def surroundingSouth(grove: list[list[str]], i: int, j: int) -> bool:
    return grove[i+1][j-1] == '#'\
    or grove[i+1][j] == '#'\
    or grove[i+1][j+1] == '#'

def surroundingWest(grove: list[list[str]], i: int, j: int) -> bool:
    return grove[i+1][j-1] == '#'\
    or grove[i][j-1] == '#'\
    or grove[i-1][j-1] == '#'

def surroundingEast(grove: list[list[str]], i: int, j: int) -> bool:
    return grove[i+1][j+1] == '#'\
    or grove[i][j+1] == '#'\
    or grove[i-1][j+1] == '#'

def surroundingAny(grove: list[list[str]], i: int, j: int) -> bool:
    return grove[i-1][j-1] == '#'\
    or grove[i-1][j] == '#'\
    or grove[i-1][j+1] == '#'\
    or grove[i][j-1] == '#'\
    or grove[i][j+1] == '#'\
    or grove[i+1][j-1] == '#'\
    or grove[i+1][j] == '#'\
    or grove[i+1][j+1] == '#'

def moveNorth(grove: list[list[str]], i: int, j: int) -> str | None:
    if not surroundingNorth(grove, i, j):
        return 'N'

def moveSouth(grove: list[list[str]], i: int, j: int) -> str | None:
    if not surroundingSouth(grove, i, j):
        return 'S'

def moveWest(grove: list[list[str]], i: int, j: int) -> str | None:
    if not surroundingWest(grove, i, j):
        return 'W'

def moveEast(grove: list[list[str]], i: int, j: int) -> str | None:
    if not surroundingEast(grove, i, j):
        return 'E'

def extend(grove: list[list[str]], by: int) -> list[list[str]]:
    grove = [by*['.'] + s + by*['.'] for s in grove]
    for _ in range(by):
        grove.insert(0, len(grove[0]) * ['.'])
        grove.append(len(grove[0]) * ['.'])
    return grove

def moveToLocation(m: Move) -> tuple[int, int]:
    match m.direction:
        case 'N':
            return (m.i-1, m.j)
        case 'S':
            return (m.i+1, m.j)
        case 'W':
            return (m.i, m.j-1)
        case 'E':
            return (m.i, m.j+1)
        case None:
            return (m.i, m.j)
        case _:
            print("oh no")
            return (0, 0)

def oneStep(grove: list[list[str]], functions):
    # what should the moves be?
    moves = []
    for i in range(len(grove)):
        for j in range(len(grove[i])):
            if grove[i][j] == '#':
                direction = None
                if surroundingAny(grove, i, j):
                    for f in functions:
                        direction = f(grove, i, j)
                        if direction is not None:
                            break
                moves.append(Move(i, j, direction))

    # decide what the new locations are
    newLocations = list(map(moveToLocation, moves))

    # find index of every duplicate location
    counts = dict(collections.Counter(newLocations))
    dupes = [key for key, value in counts.items() if value > 1]
    indecesDupes = [i for i, loc in enumerate(newLocations) if loc in dupes]

    # move
    for i, m in enumerate(moves):
        if i not in indecesDupes and m.direction is not None:
            grove[m.i][m.j] = '.'
            y, x = newLocations[i]
            grove[y][x] = '#'

    # shuffle direction order
    toEnd = functions.pop(0)
    functions.append(toEnd)

    return grove, functions

def cutOffSides(grove: list[list[str]]) -> list[list[str]]:
    coords = []
    for i in range(len(grove)):
        for j in range(len(grove[i])):
            if grove[i][j] == '#':
                coords.append((i, j))
    minI = min(map(lambda x: x[0], coords))
    maxI = max(map(lambda x: x[0], coords))
    minJ = min(map(lambda x: x[1], coords))
    maxJ = max(map(lambda x: x[1], coords))
    return [line[minJ:maxJ+1] for line in grove][minI:maxI+1]

def calculateScore(grove: list[list[str]]) -> int:
    return len(list(filter(lambda x: x == '.', sum(cutOffSides(grove), []))))

with open('input', 'r') as f:
    grove = list(map(list, f.read().splitlines()))
functions = [moveNorth, moveSouth, moveWest, moveEast]
grove = extend(grove, 20)
for i in range(10):
    grove, functions = oneStep(grove, functions)
    # printStructure(grove)
print(calculateScore(grove))
