#!/usr/bin/env python3

def dfs(adjacent_lists, visited, v):
    visited[v] = True
    for adj in adjacent_lists[v]:
        if not visited[adj]:
            dfs(adjacent_lists, visited, adj)

def find_connected_num(adjacent_lists):
    connected_sum = 0
    visited = [None] * len(adjacent_lists)
    for i in range(len(visited)):
        if not visited[i]:
            connected_sum += 1
            dfs(adjacent_lists, visited, i)
    return connected_sum

def main():
    n, e = map(int, input().split())
    adjacent_lists = [[] for _ in range(n)]
    for _ in range(e):
        v1, v2 = map(int, input().split())
        adjacent_lists[v1 - 1].append(v2 - 1)
        adjacent_lists[v2 - 1].append(v1 - 1)
    print(find_connected_num(adjacent_lists))

if __name__ == '__main__':
    main()
