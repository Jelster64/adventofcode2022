#!/bin/python
from functools import reduce
from functools import partial
import operator

class Monkey:
    alcohol = 1

    def __init__(self, startingItems, operation, modulo, tru, fls, id):
        self.items = startingItems
        self.operation = operation
        self.test = lambda n: tru if ((n % modulo) == 0) else fls
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
            return lambda n, op: int(op(n, n)) % Monkey.alcohol
        case _:
            return lambda n, op: int(op(n, int(s))) % Monkey.alcohol

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
    Monkey.alcohol *= t[0]
    return Monkey(startingItems, operation, t[0], t[1], t[2], id)

with open("input", "r") as f:
    m = list(map(parseMonkey, map(str.splitlines, f.read().split("\n\n"))))

for _ in range(10000):
    for i in range(len(m)):
        while m[i].items:
            item = m[i].takeItem()
            item = m[i].doOperation(item)
            throwTo = m[i].test(item)
            m[throwTo].throw(item)

inspections = list(map(lambda x: x.inspections, m))
inspections.sort()
part2 = reduce(operator.mul, inspections[-2:])
print(part2)
