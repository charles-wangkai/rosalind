#!/usr/bin/env python3

from queue import PriorityQueue

def read_graph():
    n, e = map(int, input().split())
    adjacent_lists = [[] for _ in range(n)]
    for _ in range(e):
        v1, v2, weight = map(int, input().split())
        adjacent_lists[v1 - 1].append((v2 - 1, weight))
    return adjacent_lists

def compute_min_dists(adjacent_lists):
    min_dists = [None] * len(adjacent_lists)
    pq = PriorityQueue()
    pq.put((0, 0))
    while not pq.empty():
        min_dist, v = pq.get()
        
        if min_dists[v] != None:
            continue
        
        min_dists[v] = min_dist
        for adj, weight in adjacent_lists[v]:
            if min_dists[adj] == None:
                pq.put((min_dists[v] + weight, adj))
    return min_dists

def main():
    print(' '.join(map(lambda x: str(x) if x != None else '-1', compute_min_dists(read_graph()))))

if __name__ == '__main__':
    main()
