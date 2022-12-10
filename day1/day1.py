#!/bin/python
file = open("input", "r").read()
elves = list(map(lambda x: sum(map(int, x)), map(str.splitlines, file.split("\n\n"))))
elves.sort()
print(max(elves), sum(elves[-3:]))
