#!/bin/python
import copy

def realIndex(i: int) -> int:
    if i == 1:
        return 0
    return int((i-1)/4)

def parseStacks(stackString: list[str]) -> list[list[str]]:
    stackString.reverse()
    amountOfStacks = int(stackString.pop(0).split()[-1])
    stacks = [[] for _ in range(amountOfStacks)]
    for line in stackString:
        line = list(line)
        for i in range(1, len(line), 4):
            if not line[i].isspace():
                stacks[realIndex(i)].append(line[i])
    return stacks

def parseMove(string: str) -> tuple[int, int, int]:
    a = string.split()
    res = list(map(int, (a[1], a[3], a[5])))
    res[1] -= 1
    res[2] -= 1
    return tuple(res)

def whatsOnTop(stacks: list[list[str]]) -> str:
    return "".join([a[-1] for a in stacks])

def crateMover9000(stacks: list[list[str]], moves: list[tuple[int, int, int]]) -> str:
    for m in moves:
        for _ in range(m[0]):
            stacks[m[2]].append(stacks[m[1]].pop())
    return whatsOnTop(stacks)

def crateMover9001(stacks: list[list[str]], moves: list[tuple[int, int, int]]) -> str:
    buffer = []
    for m in moves:
        for _ in range(m[0]):
            buffer.append(stacks[m[1]].pop())
        for _ in range(len(buffer)):
            stacks[m[2]].append(buffer.pop())
    return whatsOnTop(stacks)

stacks, moves = map(str.splitlines, open("input", "r").read().split("\n\n"))
stacks = parseStacks(stacks)
moves = list(map(parseMove, moves))
part1 = crateMover9000(copy.deepcopy(stacks), moves)
part2 = crateMover9001(stacks, moves)
print(part1, part2)
