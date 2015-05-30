#!/usr/bin/env python3

def main():
    a, b = map(int, input().split())
    print(sum(filter(lambda x: x % 2, range(a, b + 1))))

if __name__ == '__main__':
    main()
