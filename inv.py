#!/usr/bin/env python3

def count_inversion(a):
    def merge(a, b):
        nonlocal inversion_num
        
        c = []
        index_a, index_b = 0, 0
        while index_a < len(a) or index_b < len(b):
            if index_a < len(a) and (index_b == len(b) or a[index_a] <= b[index_b]):
                c.append(a[index_a])
                index_a += 1
            else:
                c.append(b[index_b])
                index_b += 1
                inversion_num += len(a) - index_a
        return c
    
    def merge_sort(a):
        size = len(a)
        if size < 2:
            return a
        return merge(merge_sort(a[:size // 2]), merge_sort(a[size // 2:]))
    
    inversion_num = 0
    merge_sort(a)
    return inversion_num

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(count_inversion(a))

if __name__ == '__main__':
    main()
