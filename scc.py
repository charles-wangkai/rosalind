#!/usr/bin/env python3

def read_graph():
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

def reverse_graph(adjacent_lists):
    reversed_adjacent_lists = [[] for _ in range(len(adjacent_lists))]
    for from_v in range(len(adjacent_lists)):
        for to_v in adjacent_lists[from_v]:
            reversed_adjacent_lists[to_v].append(from_v)
    return reversed_adjacent_lists

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

def find_strongly_connected_components(adjacent_lists):
    leave_sequences = dfs(adjacent_lists)[0]
    return dfs(reverse_graph(adjacent_lists), leave_sequences[::-1])[1]

def main():
    print(find_strongly_connected_components(read_graph()))

if __name__ == '__main__':
    main()
