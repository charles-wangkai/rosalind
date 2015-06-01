#!/usr/bin/env python3

def read_graph():
    input()
    n, e = map(int, input().split())
    adjacent_matrix = [[0] * n for _ in range(n)]
    for _ in range(e):
        v1, v2 = map(int, input().split())
        adjacent_matrix[v1 - 1][v2 - 1] = 1
        adjacent_matrix[v2 - 1][v1 - 1] = 1
    return adjacent_matrix

def multiply(a, b):
    size = len(a)
    c = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            for k in range(size):
                c[i][j] += a[i][k] * b[k][j]
    return c

def has_square(adjacent_matrix):
    two_step_reachable_matrix = multiply(adjacent_matrix, adjacent_matrix)
    size = len(two_step_reachable_matrix)
    return any([i != j and two_step_reachable_matrix[i][j] > 1 for j in range(size) for i in range(size)])

def main():
    k = int(input())
    print(' '.join(['1' if has_square(read_graph()) else '-1' for _ in range(k)]))

if __name__ == '__main__':
    main()
