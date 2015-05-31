#!/usr/bin/env python3

def read_numbers():
    _ = input()
    return list(map(int, input().split()))

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

def main():
    print(' '.join(map(str, merge(read_numbers(), read_numbers()))))

if __name__ == '__main__':
    main()
