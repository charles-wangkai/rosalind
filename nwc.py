#!/usr/bin/env python3

def read_graph():    
    while True:
        line = input()
        if line != '':
            break
    n, e = map(int, line.split())
    edges = []
    for _ in range(e):
        v1, v2, weight = map(int, input().split())
        edges.append((v1 - 1, v2 - 1, weight))
    return n, edges

def relax(min_dists, edges):
    changed = False
    for from_v, to_v, weight in edges:
        if min_dists[from_v] != None and (min_dists[to_v] == None or min_dists[to_v] > min_dists[from_v] + weight):
            min_dists[to_v] = min_dists[from_v] + weight
            changed = True
    return changed

def has_negative_weight_cycle_from_source(n, edges, source):
    min_dists = [None] * n
    min_dists[source] = 0
    
    for _ in range(n - 1):
        relax(min_dists, edges)
    
    return relax(min_dists, edges), set(filter(lambda v: min_dists[v] != None, range(n)))

def has_negative_weight_cycle(n, edges):
    sources = set(range(n))
    while sources:
        source = next(iter(sources))
        negative_weight_cycle, reachable_vertices = has_negative_weight_cycle_from_source(n, edges, source)
        
        if negative_weight_cycle:
            return True
        
        sources -= reachable_vertices
        edges = list(filter(lambda edge: edge[0] not in reachable_vertices and edge[1] not in reachable_vertices, edges))
    return False

def main():
    k = int(input())
    print(' '.join(['1' if has_negative_weight_cycle(*read_graph()) else '-1' for _ in range(k)]))

if __name__ == '__main__':
    main()
