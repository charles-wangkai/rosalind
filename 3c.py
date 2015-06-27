#!/usr/bin/env python3

import functools
import itertools

SYMBOL2NUMBER = {'A': 0, 'C': 1, 'G': 2, 'T': 3}

def find_profile_most_probable_k_mer(text, profile):
    k = len(profile[0])
    max_prob = -1
    for i in range(len(text) - k + 1):
        k_mer = text[i:i + k]
        prob = functools.reduce(lambda x, y: x * y, itertools.starmap(lambda index, symbol: profile[SYMBOL2NUMBER[symbol]][index], enumerate(k_mer)))
        if prob > max_prob:
            max_prob = prob
            most_probable_k_mer = k_mer
    return most_probable_k_mer

def main():
    text = input()
    _ = int(input())
    
    profile = []
    for _ in range(4):
        profile.append(list(map(float, input().split())))
    
    print(find_profile_most_probable_k_mer(text, profile))

if __name__ == '__main__':
    main()
