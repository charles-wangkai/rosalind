#!/usr/bin/env python3

from collections import deque

def compute_paths(adjacent_lists):
    paths = [None] * len(adjacent_lists)
    paths[0] = 0
    q = deque([0])
    while len(q):
        head = q.popleft()
        for adj in adjacent_lists[head]:
            if paths[adj] == None:
                paths[adj] = paths[head] + 1
                q.append(adj)
    return paths

def main():
    n, e = map(int, input().split())
    adjacent_lists = [[] for _ in range(n)]
    for _ in range(e):
        v1, v2 = map(int, input().split())
        adjacent_lists[v1 - 1].append(v2 - 1)
    print(' '.join(map(lambda x: str(x) if x != None else '-1', compute_paths(adjacent_lists))))

if __name__ == '__main__':
    main()
