#!/bin/python
from typing import Callable

def checkFullOverlap(a1: int, a2: int, b1: int, b2: int) -> bool:
    return (a1 <= b1 and a2 >= b2) or (a1 >= b1 and a2 <= b2)

def checkOverlap(a1: int, a2: int, b1: int, b2: int) -> bool:
    return (a2 >= b1 and a1 <= b2) or (a1 <= b2 and a2 >= b1)

def parse(string: str) -> list[int]:
    res = []
    for elf in string.split(","):
        res += elf.split("-")
    return list(map(lambda x: int(x), res))

def solve(func: Callable[[int, int ,int, int], bool], lines: list[str]) -> int:
    return sum(map(lambda x: int(func(x[0], x[1], x[2], x[3])), map(parse, lines)))

lines = open("input", "r").read().splitlines()
part1 = solve(checkFullOverlap, lines)
part2 = solve(checkOverlap, lines)
print(part1, part2)
