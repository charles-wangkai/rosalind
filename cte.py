#!/usr/bin/env python3

from queue import PriorityQueue

def read_graph():
    while True:
        line = input()
        if line != "":
            break
    n, e = map(int, line.split())
    adjacent_lists = [[] for _ in range(n)]
    through_edge = None
    for _ in range(e):
        v1, v2, weight = map(int, input().split())
        adjacent_lists[v1 - 1].append((v2 - 1, weight))
        if not through_edge:
            through_edge = (v1 - 1, v2 - 1, weight)
    return adjacent_lists, through_edge

def compute_min_dists(adjacent_lists, source):
    min_dists = [None] * len(adjacent_lists)
    pq = PriorityQueue()
    pq.put((0, source))
    while not pq.empty():
        min_dist, v = pq.get()
        
        if min_dists[v] != None:
            continue
        
        min_dists[v] = min_dist
        for adj, weight in adjacent_lists[v]:
            if min_dists[adj] == None:
                pq.put((min_dists[v] + weight, adj))
    return min_dists

def find_min_cycle_length(adjacent_lists, through_edge):
    from_v, to_v, weight = through_edge
    min_dists = compute_min_dists(adjacent_lists, to_v)
    return (weight + min_dists[from_v]) if min_dists[from_v] != None else None

def main():
    k = int(input())
    print(' '.join(map(lambda x: str(x) if x != None else '-1', [find_min_cycle_length(*read_graph()) for _ in range(k)])))

if __name__ == '__main__':
    main()
