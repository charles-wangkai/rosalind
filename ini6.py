#!/usr/bin/env python3

from collections import Counter

def main():
    for key, value in Counter(input().split()).items():
        print(key, value)

if __name__ == '__main__':
    main()
