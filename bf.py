#!/usr/bin/env python3

def read_graph():
    n, e = map(int, input().split())
    edges = []
    for _ in range(e):
        v1, v2, weight = map(int, input().split())
        edges.append((v1 - 1, v2 - 1, weight))
    return n, edges

def compute_min_dists(n, edges):
    min_dists = [None] * n
    min_dists[0] = 0
    
    for _ in range(n - 1):
        for from_v, to_v, weight in edges:
            if min_dists[from_v] != None and (min_dists[to_v] == None or min_dists[to_v] > min_dists[from_v] + weight):
                min_dists[to_v] = min_dists[from_v] + weight
    
    return min_dists

def main():
    print(' '.join(map(lambda x: str(x) if x != None else 'x', compute_min_dists(*read_graph()))))

if __name__ == '__main__':
    main()
