#!/bin/python
import networkx as nx

def charToHeight(char: str) -> int:
    match char:
        case 'S':
            return 1
        case 'E':
            return 26
        case _:
            val = ord(char)
            return val - 96

def getNeighbors(heights, x, y) -> list[tuple[str, str]]:
    res = []
    limit = heights[x][y] + 1
    current = f"{x}-{y}"
    if x < len(heights)-1 and heights[x+1][y] <= limit:
        res.append((current, f"{x+1}-{y}"))
    if x >= 1 and heights[x-1][y] <= limit:
        res.append((current, f"{x-1}-{y}"))
    if y < len(heights[x])-1 and heights[x][y+1] <= limit:
        res.append((current, f"{x}-{y+1}"))
    if y >= 1 and heights[x][y-1] <= limit:
        res.append((current, f"{x}-{y-1}"))
    return res

def constructGraph(mountain):
    heights = list(map(lambda x: list(map(charToHeight, x)), mountain))
    edges = []
    for i in range(len(heights)):
        for j in range(len(heights[i])):
            edges += getNeighbors(heights, i, j)
    graph = nx.DiGraph()
    for e in edges:
        graph.add_edge(e[0], e[1])
    return graph

def getPathLength(graph, start, goal):
    try:
        return len(nx.dijkstra_path(graph, start, goal)) - 1
    except:
        return 900000

with open("input", "r") as f:
    mountain = list(map(list, f.read().splitlines()))
startingSquares = []
S = ""
E = ""

for i in range(len(mountain)):
    for j in range(len(mountain[i])):
        match mountain[i][j]:
            case 'a':
                startingSquares.append(f"{i}-{j}")
            case 'S':
                startingSquares.append(f"{i}-{j}")
                S = f"{i}-{j}"
            case 'E':
                E = f"{i}-{j}"
            case _:
                continue

g = constructGraph(mountain)
part1 = getPathLength(g, S, E)
part2 = min(map(lambda x: getPathLength(g, x, E), startingSquares))
print(part1, part2)
