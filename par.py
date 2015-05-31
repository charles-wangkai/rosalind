#!/usr/bin/env python3

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
    a[left] = pivot

def main():
    n = int(input())
    a = list(map(int, input().split()))
    partition(a)
    print(' '.join(map(str, a)))

if __name__ == '__main__':
    main()
