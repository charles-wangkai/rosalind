#!/usr/bin/env python3

def main():
    n, e = map(int, input().split())
    degrees = [0] * n
    for _ in range(e):
        v1, v2 = map(int, input().split())
        degrees[v1 - 1] += 1
        degrees[v2 - 1] += 1
    print(' '.join(map(str, degrees)))

if __name__ == '__main__':
    main()
