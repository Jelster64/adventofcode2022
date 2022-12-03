#!/bin/python
lines = open("input", "r").readlines()
elves = []
count = 0
for line in lines:
    if line.isspace():
        elves.append(count)
        count = 0
    else:
        count += int(line)
elves.append(count)
print(max(elves))
