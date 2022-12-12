#!/bin/python
from functools import reduce
from functools import partial
import operator

class Monkey:
    def __init__(self, startingItems, operation, test, id):
        self.items = startingItems
        self.operation = operation
        self.test = test
        self.inspections: int = 0
        self.id = id

    def throw(self, item: int):
        self.items.append(item)

    def takeItem(self):
        return self.items.pop(0)

    def doOperation(self, item: int) -> int:
        self.inspections += 1
        return self.operation(item)


def partialOperation(s: str):
    match s:
        case "old":
            return lambda n, op: int(op(n, n) / 3)
        case _:
            return lambda n, op: int(op(n, int(s)) / 3)

def parseOperation(args: list[str]):
    res = partialOperation(args[-1])
    match args[3]:
        case "*":
            return partial(res, op=operator.mul)
        case "+":
            return partial(res, op=operator.add)
        case "-":
            return partial(res, op=operator.sub)
        case _:
            print(f"couldn't parse operation {args[3]}")
            return partial(res, op=operator.add)


def parseMonkey(monkey):
    id = int(monkey[0][7])
    monkey = list(map(lambda s: s.split(": ")[1], monkey[1:]))
    startingItems = list(map(int, str(monkey[0]).split(", ")))
    operation = parseOperation(monkey[1].split())
    t = list(map(lambda a: int(a[-1]), map(str.split, monkey[2:])))
    test = lambda n: t[1] if ((n % t[0]) == 0) else t[2]
    return Monkey(startingItems, operation, test, id)

with open("input", "r") as f:
    m = list(map(parseMonkey, map(str.splitlines, f.read().split("\n\n"))))

for i in range(len(m)):
    assert(i == m[i].id)

for _ in range(20):
    for i in range(len(m)):
        while m[i].items:
            item = m[i].takeItem()
            item = m[i].doOperation(item)
            throwTo = m[i].test(item)
            m[throwTo].throw(item)

inspections = list(map(lambda x: x.inspections, m))
inspections.sort()
part1 = reduce(operator.mul, inspections[-2:])
print(part1)
