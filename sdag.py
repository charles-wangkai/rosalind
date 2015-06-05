#!/usr/bin/env python3

def read_graph():
    n, e = map(int, input().split())
    from_lists = [set() for _ in range(n)]
    to_lists = [[] for _ in range(n)]
    edges = {}
    for _ in range(e):
        v1, v2, weight = map(int, input().split())
        from_lists[v2 - 1].add(v1 - 1)
        to_lists[v1 - 1].append(v2 - 1)
        edges[(v1 - 1, v2 - 1)] = weight
    return from_lists, to_lists, edges

def dfs(from_lists, to_lists, visited, sequence, v):
    visited[v] = True
    sequence.append(v)
    for adj in to_lists[v]:
        if not visited[adj]:
            from_lists[adj].discard(v)
            if len(from_lists[adj]) == 0:
                dfs(from_lists, to_lists, visited, sequence, adj)

def topological_sort(from_lists, to_lists):
    visited = [False] * len(from_lists)
    sequence = []
    for i in range(len(visited)):
        if not visited[i] and len(from_lists[i]) == 0:
            dfs(from_lists, to_lists, visited, sequence, i)
    return sequence

def compute_min_dists(from_lists, to_lists, edges):
    min_dists = [None] * len(from_lists)
    min_dists[0] = 0
    
    sequence = topological_sort(from_lists, to_lists)
    
    for from_v in sequence:
        if min_dists[from_v] != None:
            for to_v in to_lists[from_v]:
                if min_dists[to_v] == None or min_dists[to_v] > min_dists[from_v] + edges[(from_v, to_v)]:
                    min_dists[to_v] = min_dists[from_v] + edges[(from_v, to_v)]
                
    return min_dists

def main():
    print(' '.join(map(lambda x: str(x) if x != None else 'x', compute_min_dists(*read_graph()))))

if __name__ == '__main__':
    main()
