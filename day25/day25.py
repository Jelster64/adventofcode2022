#!/bin/python
import operator
from functools import reduce

def snafuDigitToDecimal(c: str) -> int:
    match c:
        case '=':
            return -2
        case '-':
            return -1
        case '0':
            return 0
        case '1':
            return 1
        case '2':
            return 2
        case _:
            print("uh oh")
            return 9

def decimalDigitToSnafu(i: int) -> str:
    match i:
        case -2:
            return '='
        case -1:
            return '-'
        case 0:
            return '0'
        case 1:
            return '1'
        case 2:
            return '2'
        case _:
            print("uh oh")
            return '9'

def snafuToDecimal(s: list[str]) -> int:
    res = 0
    for i, n in enumerate(s):
        res += pow(5, i) * snafuDigitToDecimal(n)
    return res

def decimalToQuinary(n: int) -> str:
    res = ''
    amountOfDigits = 0
    while pow(5, amountOfDigits + 1) < n:
        amountOfDigits += 1
    for i in range(amountOfDigits, -1, -1):
        quotient, n = divmod(n, pow(5, i))
        res += str(quotient)
    return res

def quinaryToSnafu(s: str) -> str:
    s = list(map(int, list(reversed(s))))
    for i, c in enumerate(s):
        if c > 4:
            s[i] = c-5
            s[i+1] = s[i+1]+1
        if c == 3:
            s[i] = -2
            s[i+1] = s[i+1] + 1
        if c == 4:
            s[i] = -1
            s[i+1] = s[i+1] + 1
    return reduce(operator.add, reversed(list(map(decimalDigitToSnafu, s))))

with open('input', 'r') as f:
    snafuNums = [list(reversed(s)) for s in f.read().splitlines()]
part1 = quinaryToSnafu(decimalToQuinary(sum(map(snafuToDecimal, snafuNums))))
print(part1)
