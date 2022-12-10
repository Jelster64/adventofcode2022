#!/bin/python
import operator
from functools import reduce
from functools import partial

def toSize(obj) -> int:
    match obj:
        case int():
            return obj
        case Dir():
            return obj.getSize()
        case _:
            print("wrong type")
            return 0

class Dir:
    def __init__(self, name: str, parent):
        self.name = name
        self.contents = []
        self.parent = parent
        self.size: int = -1

    def add(self, elem):
        self.contents.append(elem)

    def getSize(self) -> int:
        if self.size == -1:
            self.size = sum(map(toSize, self.contents))
        return self.size

def cd(workingDir: Dir, name: str) -> Dir:
    if name == "..":
        return workingDir.parent
    for item in workingDir.contents:
        if type(item) == Dir:
            if item.name == name:
                return item
    print("error")
    return Dir("uh oh", None)

def parseDirectoryStructure(root: Dir):
    lsMode = False
    workingDirectory: Dir = root
    for c in commands:
        if lsMode:
            match c[0]:
                case "$":
                    lsMode = False
                case "dir":
                    workingDirectory.add(Dir(c[1], workingDirectory))
                    continue
                case _:
                    workingDirectory.add(int(c[0]))
                    continue
        assert(c[0] == "$")
        match c[1]:
            case "cd":
                workingDirectory = cd(workingDirectory, c[2])
            case "ls":
                lsMode = True

def sumDirsLessThan(d, limit: int) -> int:
    match d:
        case Dir():
            sizeChildren = sum(map(partial(sumDirsLessThan, limit=limit), d.contents))
            if d.getSize() <= limit:
                return d.getSize() + sizeChildren
            return sizeChildren
        case _:
            return 0

def dirsToSizes(d) -> list[int]:
    match d:
        case Dir():
            return [d.getSize()] + list(reduce(operator.add, map(dirsToSizes, d.contents)))
        case _:
            return []

def getSmallestBigFile(root: Dir, totalSpace: int, neededUnusedSpace: int) -> int:
    minimumDirSize = neededUnusedSpace - (totalSpace - root.getSize())
    return min(filter(lambda x: x >= minimumDirSize, dirsToSizes(root)))

with open("input", "r") as f:
    commands = list(map(str.split, f.read().splitlines()[1:]))
root: Dir = Dir("/", None)
parseDirectoryStructure(root)
part1 = sumDirsLessThan(root, 100000)
part2 = getSmallestBigFile(root, 70000000, 30000000)
print(part1, part2)
