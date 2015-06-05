#!/usr/bin/env python3

def read_graph():
    input()
    n, e = map(int, input().split())
    adjacent_lists = [[] for _ in range(n)]
    for _ in range(e):
        v1, v2 = map(int, input().split())
        adjacent_lists[v1 - 1].append(v2 - 1)
    return adjacent_lists

def search(adjacent_lists, visited, leave_sequences, v):
    visited[v] = True
    for adj in adjacent_lists[v]:
        if not visited[adj]:
            search(adjacent_lists, visited, leave_sequences, adj)
    leave_sequences.append(v)

def dfs(adjacent_lists, sources=None):
    if sources == None:
        sources = range(len(adjacent_lists))
    
    visited = [False] * len(adjacent_lists)
    leave_sequences = []
    tree_num = 0
    for source in sources:
        if not visited[source]:
            tree_num += 1
            search(adjacent_lists, visited, leave_sequences, source)
    return leave_sequences, tree_num

def is_general_sink(adjacent_lists, source):
    sources = list(range(len(adjacent_lists)))
    sources[0], sources[source] = sources[source], sources[0]
    
    return dfs(adjacent_lists, sources)[1] == 1

def find_general_sink(adjacent_lists):
    leave_sequences = dfs(adjacent_lists)[0]
    return leave_sequences[-1] if is_general_sink(adjacent_lists, leave_sequences[-1]) else None

def main():
    k = int(input())
    print(' '.join(map(lambda v: str(v + 1) if v != None else '-1', [find_general_sink(read_graph()) for _ in range(k)])))

if __name__ == '__main__':
    main()
