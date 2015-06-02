#!/usr/bin/env python3

import random

def partition(a):
    pivot = a[0]
    left, right = 0, len(a) - 1
    while left != right:
        while right != left and a[right] > pivot:
            right -= 1
        a[left], a[right] = a[right], a[left]
        while left != right and a[left] <= pivot:
            left += 1
        a[left], a[right] = a[right], a[left]
    return left

def find_kth_smallest_element(a, k):
    index = random.randrange(len(a))
    a[0], a[index] = a[index], a[0]
    
    pos = partition(a)
    if pos == k - 1:
        return a[pos]
    elif pos < k - 1:
        return find_kth_smallest_element(a[pos + 1:], k - pos - 1)
    else:
        return find_kth_smallest_element(a[:pos], k)

def main():
    n = int(input())
    a = list(map(int, input().split()))
    k = int(input())
    print(find_kth_smallest_element(a, k))

if __name__ == '__main__':
    main()
