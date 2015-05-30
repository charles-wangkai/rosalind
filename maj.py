#!/usr/bin/env python3

def check_majority(a, candidate):
    return len(list(filter(lambda x: x == candidate, a))) * 2 > len(a)

def find_majority(a):
    candidate, count = None, 0
    for number in a:
        if count == 0:
            candidate, count = number, 1
        elif number == candidate:
            count += 1
        else:
            count -= 1
    return candidate if check_majority(a, candidate) else -1

def main():
    k, n = map(int, input().split())
    print(' '.join(str(find_majority(list(map(int, input().split())))) for _ in range(k)))

if __name__ == '__main__':
    main()
