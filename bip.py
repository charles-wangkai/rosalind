#!/usr/bin/env python3

def read_graph():
    input()
    n, e = map(int, input().split())
    adjacent_lists = [[] for _ in range(n)]
    for _ in range(e):
        v1, v2 = map(int, input().split())
        adjacent_lists[v1 - 1].append(v2 - 1)
        adjacent_lists[v2 - 1].append(v1 - 1)
    return adjacent_lists

def paint(adjacent_lists, colors, v, color):
    if colors[v] != None:
        return colors[v] == color
    
    colors[v] = color
    for adj in adjacent_lists[v]:
        if not paint(adjacent_lists, colors, adj, not color):
            return False
    return True

def is_bipartite(adjacent_lists):
    colors = [None] * len(adjacent_lists)
    for i in range(len(colors)):
        if colors[i] == None:
            if not paint(adjacent_lists, colors, i, True):
                return False
    return True

def main():
    k = int(input())
    print(' '.join(['1' if is_bipartite(read_graph()) else '-1' for _ in range(k)]))

if __name__ == '__main__':
    main()
