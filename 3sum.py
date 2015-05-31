#!/usr/bin/env python3

def find_triple(a):
    number2indices = {}
    for i in range(len(a)):
        if a[i] not in number2indices:
            number2indices[a[i]] = set()
        number2indices[a[i]].add(i)
    
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            target = -a[i] - a[j]
            if target in number2indices:
                indices = list(filter(lambda x: x != i and x != j, number2indices[target]))
                if indices:
                    return i, j, indices[0]

def main():
    k, n = map(int, input().split())
    for _ in range(k):
        indices = find_triple(list(map(int, input().split())))
        if indices:
            print(' '.join(map(lambda x: str(x + 1), indices)))
        else:
            print(-1)

if __name__ == '__main__':
    main()
