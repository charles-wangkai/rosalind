#!/usr/bin/env python3

import sys

RECURSION_LIMIT = 2500

def read_formula():
    input()
    n, m = map(int, input().split())
    
    variables = {x: None for x in range(-n, n + 1) if x != 0}
    adjacent_lists = {x: [] for x in range(-n, n + 1) if x != 0}
    
    for _ in range(m):
        a, b = map(int, input().split())
        adjacent_lists[-a].append(b)
        adjacent_lists[-b].append(a)
    return variables, adjacent_lists

def contains_mutual_negative(strongly_connected_component):
    for x in strongly_connected_component:
        if -x in strongly_connected_component:
            return True
    return False

def search(adjacent_lists, visited, leave_sequences, tree_set, v):
    visited[v] = True
    for adj in adjacent_lists[v]:
        if not visited[adj]:
            search(adjacent_lists, visited, leave_sequences, tree_set, adj)
    leave_sequences.append(v)
    tree_set.add(v)

def dfs(adjacent_lists, sources=None):
    if sources == None:
        sources = adjacent_lists.keys()
    
    visited = {x: False for x in adjacent_lists}
    leave_sequences = []
    tree_sets = []
    for source in sources:
        if not visited[source]:
            tree_set = set()
            search(adjacent_lists, visited, leave_sequences, tree_set, source)
            tree_sets.append(tree_set)
    return leave_sequences, tree_sets

def reverse_graph(adjacent_lists):
    n = len(adjacent_lists) // 2
    reversed_adjacent_lists = {x: [] for x in range(-n, n + 1) if x != 0}
    for from_v in adjacent_lists:
        for to_v in adjacent_lists[from_v]:
            reversed_adjacent_lists[to_v].append(from_v)
    return reversed_adjacent_lists

def find_strongly_connected_components(adjacent_lists):
    leave_sequences = dfs(adjacent_lists)[0]
    return dfs(reverse_graph(adjacent_lists), leave_sequences[::-1])[1]

def is_assigned(variables, strongly_connected_component):
    return any(map(lambda x: variables[x] != None, strongly_connected_component))

def find_assignment(variables, adjacent_lists):
    strongly_connected_components = find_strongly_connected_components(adjacent_lists)
    
    if any(map(contains_mutual_negative, strongly_connected_components)):
        return None
    
    variable2strongly_connected_component = {}
    for strongly_connected_component in strongly_connected_components:
        for x in strongly_connected_component:
            variable2strongly_connected_component[x] = strongly_connected_component
    
    for strongly_connected_component in strongly_connected_components[::-1]:
        if not is_assigned(variables, strongly_connected_component):
            for x in strongly_connected_component:
                variables[x] = True
                variables[-x] = False
    
    return [x if variables[x] else -x for x in range(1, len(variables) // 2 + 1)]

def main():
    sys.setrecursionlimit(RECURSION_LIMIT)
    
    k = int(input())
    for _ in range(k):
        assignment = find_assignment(*read_formula())
        
        if assignment != None:
            print(1, ' '.join(map(str, assignment)))
        else:
            print(0)

if __name__ == '__main__':
    main()
