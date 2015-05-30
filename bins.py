#!/usr/bin/env python3

def find(a, k):
    lower, upper = 0, len(a) - 1
    while lower <= upper:
        middle = (lower + upper) // 2
        if a[middle] == k:
            return middle + 1
        elif a[middle] < k:
            lower = middle + 1
        else:
            upper = middle - 1
    return -1

def main():
    n = int(input())
    m = int(input())
    a = list(map(int, input().split()))
    print(' '.join([str(find(a, k)) for k in map(int, input().split())]))

if __name__ == '__main__':
    main()
