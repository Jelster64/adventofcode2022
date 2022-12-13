#!/bin/python
with open("input", "r") as f:
    elves = sorted(list(map(lambda x: sum(map(int, x)), map(str.splitlines, f.read().split("\n\n")))))
print(max(elves), sum(elves[-3:]))
