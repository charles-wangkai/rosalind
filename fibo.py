#!/usr/bin/env python3

def main():
    n = int(input())
    prev = 1
    fib = 0
    for _ in range(n):
        prev, fib = fib, prev + fib
    print(fib)

if __name__ == '__main__':
    main()
