#!/bin/python
import copy

class Move:
    def __init__(self, amount: int, source: int, dest: int):
        self.amount = amount
        self.source = source
        self.dest = dest

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

def parseMove(string: str) -> Move:
    a = string.split()
    return Move(int(a[1]), int(a[3])-1, int(a[5])-1)

def stackMove(source: list[str], dest: list[str]) -> None:
    dest.append(source.pop())

def whatsOnTop(stacks: list[list[str]]) -> str:
    return "".join([a[-1] for a in stacks])

def crateMover9000(stacks: list[list[str]], moves: list[Move]) -> str:
    for m in moves:
        for _ in range(m.amount):
            stackMove(stacks[m.source], stacks[m.dest])
    return whatsOnTop(stacks)

def crateMover9001(stacks: list[list[str]], moves: list[Move]) -> str:
    buffer = []
    for m in moves:
        for _ in range(m.amount):
            stackMove(stacks[m.source], buffer)
        for _ in range(len(buffer)):
            stackMove(buffer, stacks[m.dest])
    return whatsOnTop(stacks)

stacks, moves = map(str.splitlines, open("input", "r").read().split("\n\n"))
stacks = parseStacks(stacks)
moves = list(map(parseMove, moves))
part1 = crateMover9000(copy.deepcopy(stacks), moves)
part2 = crateMover9001(stacks, moves)
print(part1, part2)
