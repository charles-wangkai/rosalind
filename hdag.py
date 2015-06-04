#!/usr/bin/env python3

def read_graph():
    while True:
        line = input()
        if line != "":
            break
    n, e = map(int, line.split())
    from_lists = [set() for _ in range(n)]
    to_lists = [set() for _ in range(n)]
    for _ in range(e):
        v1, v2 = map(int, input().split())
        from_lists[v2 - 1].add(v1 - 1)
        to_lists[v1 - 1].add(v2 - 1)
    return from_lists, to_lists

def dfs(from_lists, to_lists, visited, sequence, v):
    visited[v] = True
    sequence.append(v)
    for adj in to_lists[v]:
        if not visited[adj]:
            from_lists[adj].remove(v)
            if len(from_lists[adj]) == 0:
                dfs(from_lists, to_lists, visited, sequence, adj)

def topological_sort(from_lists, to_lists):
    visited = [False] * len(from_lists)
    sequence = []
    for i in range(len(visited)):
        if not visited[i] and len(from_lists[i]) == 0:
            dfs(from_lists, to_lists, visited, sequence, i)
    return sequence

def is_hamiltonian_path(path, to_lists):
    for i in range(len(path) - 1):
        if path[i + 1] not in to_lists[path[i]]:
            return False
    return True

def find_hamiltonian_path(from_lists, to_lists):
    sequence = topological_sort(from_lists, to_lists)
    return sequence if is_hamiltonian_path(sequence, to_lists) else None

def main():
    k = int(input())
    for _ in range(k):
        hamiltonian_path = find_hamiltonian_path(*read_graph())
        if hamiltonian_path:
            print(1, ' '.join(map(lambda v: str(v + 1), hamiltonian_path)))
        else:
            print(-1)

if __name__ == '__main__':
    main()
