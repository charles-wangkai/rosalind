#!/usr/bin/env python3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    k = int(input())
    
    print(' '.join(map(str, sorted(a)[:k])))

if __name__ == '__main__':
    main()
