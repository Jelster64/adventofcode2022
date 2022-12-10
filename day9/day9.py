#!/bin/python

class Position:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def move(self, direction: str):
        match direction:
            case "U":
                self.y += 1
            case "D":
                self.y -= 1
            case "R":
                self.x += 1
            case "L":
                self.x -= 1
            case _:
                print("error")

    def chaseOtherPosition(self, other):
        if self.x < other.x:
            self.x += 1
        elif self.x > other.x:
            self.x -= 1
        if self.y < other.y:
            self.y += 1
        elif self.y > other.y:
            self.y -= 1

    def isTouching(self, other) -> bool:
        return abs(self.x - other.x) < 2 and abs(self.y - other.y) < 2

class Move:
    def __init__(self, direction: str, steps: int):
        self.direction = direction
        self.steps = steps

def countUniqueTailPositions(moves: list[Move], ropeLength: int) -> int:
    tailPositions = set()
    rope = [Position(0, 0) for _ in range(ropeLength)]
    tailPositions.add((rope[-1].x, rope[-1].y))
    for move in moves:
        for _ in range(move.steps):
            rope[0].move(move.direction)
            for i in range(1, len(rope)):
                if not rope[i].isTouching(rope[i-1]):
                    rope[i].chaseOtherPosition(rope[i-1])
            tailPositions.add((rope[-1].x, rope[-1].y))
    return len(tailPositions)

with open("input", "r") as f:
    moves = list(map(lambda m: Move(m[0], int(m[1])), map(str.split, f.read().splitlines())))
part1 = countUniqueTailPositions(moves, 2)
part2 = countUniqueTailPositions(moves, 10)
print(part1, part2)
