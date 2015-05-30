#!/usr/bin/env python3

def main():
    n, e = map(int, input().split())
    degrees = [0] * n
    adjacent_lists = [[] for _ in range(n)]
    for _ in range(e):
        v1, v2 = map(int, input().split())
        degrees[v1 - 1] += 1
        degrees[v2 - 1] += 1
        adjacent_lists[v1 - 1].append(v2 - 1)
        adjacent_lists[v2 - 1].append(v1 - 1)
    print(' '.join(str(sum(map(lambda v: degrees[v], adjacent_lists[i]))) for i in range(n)))

if __name__ == '__main__':
    main()
