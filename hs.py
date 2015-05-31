#!/usr/bin/env python3

def sift_down(a, heap_size, v):
    while True:
        max_node = v
        if v * 2 + 1 < heap_size and a[v * 2 + 1] > a[max_node]:
            max_node = v * 2 + 1
        if v * 2 + 2 < heap_size and a[v * 2 + 2] > a[max_node]:
            max_node = v * 2 + 2
        if max_node == v:
            break
        a[v], a[max_node] = a[max_node], a[v]
        v = max_node

def build_max_heap(a):
    for i in range(len(a) - 1, 0, -1):
        parent = (i - 1) // 2
        if a[i] > a[parent]:
            a[parent], a[i] = a[i], a[parent]
            sift_down(a, len(a), i)

def heap_sort(a):
    build_max_heap(a)
    
    for heap_size in range(len(a), 1, -1):
        a[0], a[heap_size - 1] = a[heap_size - 1], a[0]
        sift_down(a, heap_size - 1, 0)

def main():
    n = int(input())
    a = list(map(int, input().split()))
    heap_sort(a)
    print(' '.join(map(str, a)))

if __name__ == '__main__':
    main()
