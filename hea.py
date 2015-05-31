#!/usr/bin/env python3

def build_max_heap(a):
    for i in range(len(a) - 1, 0, -1):
        parent = (i - 1) // 2
        if a[i] > a[parent]:
            a[parent], a[i] = a[i], a[parent]
            
            v = i
            while True:
                max_node = v
                if v * 2 + 1 < len(a) and a[v * 2 + 1] > a[max_node]:
                    max_node = v * 2 + 1
                if v * 2 + 2 < len(a) and a[v * 2 + 2] > a[max_node]:
                    max_node = v * 2 + 2
                if max_node == v:
                    break
                a[v], a[max_node] = a[max_node], a[v]
                v = max_node

def main():
    n = int(input())
    a = list(map(int, input().split()))
    build_max_heap(a)
    print(' '.join(map(str, a)))

if __name__ == '__main__':
    main()
