#!/bin/python

def isImportantCycle1(cycle: int) -> bool:
    return cycle >= 20 and cycle <= 220 and cycle % 40 == 20

def signalStrengths(instructions: list[list[str]]) -> int:
    x = 1
    cycle = 1
    res = []
    for ins in instructions:
        cycle += 1
        if isImportantCycle1(cycle):
            res.append(cycle * x)
        match ins[0]:
            case "noop":
                continue
            case "addx":
                cycle += 1
                x += int(ins[1])
                if isImportantCycle1(cycle):
                    res.append(cycle * x)
            case _:
                print("bad syntax")
    return sum(res)

def pixel(cycle: int, sprite: int) -> str:
    location = (cycle-1) % 40
    if (location >= sprite-1 and location <= sprite+1):
        return '#'
    return '.'

def isImportantCycle2(cycle: int) -> bool:
    return cycle >= 40 and cycle <= 220 and (cycle % 40 == 1)

def crt(instructions: list[list[str]]) -> str:
    sprite = 1
    cycle = 1
    crt = [[] for _ in range(6)]
    scanline = 0
    for ins in instructions:
        if isImportantCycle2(cycle):
            scanline += 1
        crt[scanline].append(pixel(cycle, sprite))
        cycle += 1
        match ins[0]:
            case "noop":
                continue
            case "addx":
                if isImportantCycle2(cycle):
                    scanline += 1
                crt[scanline].append(pixel(cycle, sprite))
                cycle += 1
                sprite += int(ins[1])
            case _:
                print("bad syntax")
    return "\n".join(map("".join, crt))

with open("input", "r") as f:
    instructions = list(map(str.split, f.read().splitlines()))
part1 = signalStrengths(instructions)
part2 = crt(instructions)
print(f"{part1}\n{part2}")
