#!/usr/bin/env python3

def find_pair(a):
    history = {}
    for i in range(len(a)):
        if -a[i] in history:
            return history[-a[i]], i
        history[a[i]] = i
    return None

def main():
    k, n = map(int, input().split())
    for _ in range(k):
        indices = find_pair(list(map(int, input().split())))
        if indices:
            print(indices[0] + 1, indices[1] + 1)
        else:
            print(-1)

if __name__ == '__main__':
    main()
