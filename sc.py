#!/usr/bin/env python3

def read_graph():
    input()
    n, e = map(int, input().split())
    adjacent_lists = [[] for _ in range(n)]
    edges = set()
    for _ in range(e):
        v1, v2 = map(int, input().split())
        adjacent_lists[v1 - 1].append(v2 - 1)
        edges.add((v1 - 1, v2 - 1))
    return adjacent_lists, edges

def search(adjacent_lists, visited, leave_sequences, tree_set, v):
    visited[v] = True
    for adj in adjacent_lists[v]:
        if not visited[adj]:
            search(adjacent_lists, visited, leave_sequences, tree_set, adj)
    leave_sequences.append(v)
    tree_set.add(v)

def dfs(adjacent_lists, sources=None):
    if sources == None:
        sources = range(len(adjacent_lists))
    
    visited = [False] * len(adjacent_lists)
    leave_sequences = []
    tree_sets = []
    for source in sources:
        if not visited[source]:
            tree_set = set()
            search(adjacent_lists, visited, leave_sequences, tree_set, source)
            tree_sets.append(tree_set)
    return leave_sequences, tree_sets

def reverse_graph(adjacent_lists):
    reversed_adjacent_lists = [[] for _ in range(len(adjacent_lists))]
    for from_v in range(len(adjacent_lists)):
        for to_v in adjacent_lists[from_v]:
            reversed_adjacent_lists[to_v].append(from_v)
    return reversed_adjacent_lists

def find_strongly_connected_components(adjacent_lists):
    leave_sequences = dfs(adjacent_lists)[0]
    return dfs(reverse_graph(adjacent_lists), leave_sequences[::-1])[1]

def has_edge_between(edges, from_strongly_connected_component, to_strongly_connected_component):
    for from_v in from_strongly_connected_component:
        for to_v in to_strongly_connected_component:
            if (from_v, to_v) in edges:
                return True
    return False

def is_semi_connected(adjacent_lists, edges):
    strongly_connected_components = find_strongly_connected_components(adjacent_lists)
    
    for i in range(len(strongly_connected_components) - 1):
        if not has_edge_between(edges, strongly_connected_components[i], strongly_connected_components[i + 1]):
            return False
    return True

def main():
    k = int(input())
    print(' '.join(['1' if is_semi_connected(*read_graph()) else '-1' for _ in range(k)]))

if __name__ == '__main__':
    main()
