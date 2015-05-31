#!/usr/bin/env python3

def merge(a, b):
    c = []
    index_a, index_b = 0, 0
    while index_a < len(a) or index_b < len(b):
        if index_a < len(a) and (index_b == len(b) or a[index_a] <= b[index_b]):
            c.append(a[index_a])
            index_a += 1
        else:
            c.append(b[index_b])
            index_b += 1
    return c

def merge_sort(a):
    size = len(a)
    if size < 2:
        return a
    return merge(merge_sort(a[:size // 2]), merge_sort(a[size // 2:]))

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(' '.join(map(str, merge_sort(a))))

if __name__ == '__main__':
    main()
