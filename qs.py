#!/usr/bin/env python3

import random

def partition(a, begin, end):
    pivot = a[begin]
    left, right = begin, end
    while left != right:
        while right != left and a[right] > pivot:
            right -= 1
        a[left], a[right] = a[right], a[left]
        while left != right and a[left] <= pivot:
            left += 1
        a[left], a[right] = a[right], a[left]
    return left

def quick_sort(a, begin=0, end=None):
    if end == None:
        end = len(a) - 1
    
    if begin > end:
        return
    
    index = random.randrange(begin, end + 1)
    a[begin], a[index] = a[index], a[begin]
    
    pos = partition(a, begin, end)    
    quick_sort(a, begin, pos - 1)
    quick_sort(a, pos + 1, end)

def main():
    n = int(input())
    a = list(map(int, input().split()))
    quick_sort(a)
    print(' '.join(map(str, a)))

if __name__ == '__main__':
    main()
