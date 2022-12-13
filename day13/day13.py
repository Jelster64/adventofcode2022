#!/bin/python
import ast
from functools import reduce
from functools import cmp_to_key
import operator

def compareWrapper(one, two) -> int:
    match compare(one, two):
        case True:
            return -1
        case None:
            return 0
        case False:
            return 1

def compare(one, two) -> bool | None:
    match one, two:
        case int(), int():
            if one != two:
                return one < two
            return None
        case int(), list():
            return compare([one], two)
        case list(), int():
            return compare(one, [two])
        case list(), list():
            for left, right in zip(one, two):
                res = compare(left, right)
                if res == None:
                    continue
                return res
            if len(one) == len(two):
                return None
            return len(one) <= len(two)

def pairsOfPackets(packets) -> int:
    res = 0
    rightOrder = list(map(lambda x: reduce(compare, x), packets))
    for i, b in enumerate(rightOrder, 1):
        if b:
            res += i
    return res

def decoderKey(packets) -> int:
    res = 1
    packets += [[[[2]], [[6]]]]
    sortedPackets = sorted(list(reduce(operator.add, packets)), key=cmp_to_key(compareWrapper))
    for i, p in enumerate(sortedPackets, 1):
        match p:
            case [[2]] | [[6]]:
                res *= i
    return res

with open("input", "r") as f:
    packets = list(map(lambda x: list(map(ast.literal_eval, x)), map(str.splitlines, f.read().split("\n\n"))))
part1 = pairsOfPackets(packets)
part2 = decoderKey(packets)
print(part1, part2)
