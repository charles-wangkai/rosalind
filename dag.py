#!/usr/bin/env python3

def read_graph():
    input()
    n, e = map(int, input().split())
    from_lists = [set() for _ in range(n)]
    to_lists = [[] for _ in range(n)]
    for _ in range(e):
        v1, v2 = map(int, input().split())
        from_lists[v2 - 1].add(v1 - 1)
        to_lists[v1 - 1].append(v2 - 1)
    return from_lists, to_lists

def dfs(from_lists, to_lists, visited, v):
    visited[v] = True
    for adj in to_lists[v]:
        if not visited[adj]:
            from_lists[adj].remove(v)
            if len(from_lists[adj]) == 0:
                dfs(from_lists, to_lists, visited, adj)

def is_acyclic(from_lists, to_lists):
    visited = [False] * len(from_lists)
    for i in range(len(visited)):
        if not visited[i] and len(from_lists[i]) == 0:
            dfs(from_lists, to_lists, visited, i)
    return all(visited)

def main():
    k = int(input())
    print(' '.join(['1' if is_acyclic(*read_graph()) else '-1' for _ in range(k)]))

if __name__ == '__main__':
    main()
