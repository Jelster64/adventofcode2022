#!/bin/python
import re, collections

Me = collections.namedtuple('Me', ['x', 'y', 'direction'])

def printStructure(structure):
    print('\n'.join([''.join(s) for s in structure]))

def routeParser(item: str):
    match item:
        case 'L'|'R':
            return item
        case _:
            return int(item)

def addPadding(board: list[list[str]]) -> list[list[str]]:
    longestRow = max(map(len, board))
    for row in board:
        if len(row) < longestRow:
            row += [' ']*(longestRow - len(row))
    return board

def turn(me: Me, turn: str) -> Me:
    match me.direction, turn:
        case ('left', 'L') | ('right', 'R'):
            return Me(me.x, me.y, 'down')
        case ('right', 'L') | ('left', 'R'):
            return Me(me.x, me.y, 'up')
        case ('up', 'L') | ('down', 'R'):
            return Me(me.x, me.y, 'left')
        case ('down', 'L') | ('up', 'R'):
            return Me(me.x, me.y, 'right')
        case _:
            print('uh oh (can\'t turn)')
            return me

def move(me: Me, steps: int, board: list[list[str]]) -> Me:
    if steps == 0:
        return me
    # do one step. if it's oob, find new spot after wraparound
    match me.direction:
        case 'up':
            newMe = Me(me.x, me.y-1, me.direction)
            if newMe.y < 0 or board[newMe.y][newMe.x] == ' ':
                i = len(board)-1
                while board[i][me.x] == ' ':
                    i -= 1
                newMe = Me(me.x, i, me.direction)
        case 'down':
            newMe = Me(me.x, me.y+1, me.direction)
            if newMe.y >= len(board) or board[newMe.y][newMe.x] == ' ':
                i = 0
                while board[i][me.x] == ' ':
                    i += 1
                newMe = Me(me.x, i, me.direction)
        case 'left':
            newMe = Me(me.x-1, me.y, me.direction)
            if newMe.x < 0 or board[newMe.y][newMe.x] == ' ':
                i = len(board[me.y])-1
                while board[me.y][i] == ' ':
                    i -= 1
                newMe = Me(i, me.y, me.direction)
        case 'right':
            newMe = Me(me.x+1, me.y, me.direction)
            if newMe.x >= len(board[0]) or board[newMe.y][newMe.x] == ' ':
                i = 0
                while board[me.y][i] == ' ':
                    i += 1
                newMe = Me(i, me.y, me.direction)
        case _:
            print('uh oh (not up, down, left, right)')
            return me

    match board[newMe.y][newMe.x]:
        case '#':
            return me
        case '.':
            return move(newMe, steps-1, board)
        case _:
            print('uh oh (bad board value)')
            return me

def calculateScore(me: Me) -> int:
    d = {'right': 0, 'down': 1, 'left': 2, 'up': 3}
    return 1000 * (me.y+1) + 4 * (me.x+1) + d.get(me.direction)

def followTheRoute(route: list[int|str], board: list[list[str]]) -> int:
    me = Me(board[0].index('.'), 0, 'right')
    for r in route:
        match r:
            case 'L'|'R':
                me = turn(me, r)
            case int():
                me = move(me, r, board)
            case _:
                print('uh oh')
    return calculateScore(me)

with open('input', 'r') as f:
    rawBoard, rawRoute = f.read().split('\n\n')
    route = list(map(routeParser, re.findall(r'\d+|L|R', rawRoute)))
    board = addPadding(list(map(list, rawBoard.splitlines())))
part1 = followTheRoute(route, board)
print(part1)
