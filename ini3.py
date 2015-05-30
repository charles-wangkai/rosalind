#!/usr/bin/env python3

def main():
    s = input()
    a, b, c, d = map(int, input().split())
    print(s[a:b + 1], s[c:d + 1])

if __name__ == '__main__':
    main()
