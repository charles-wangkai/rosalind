#!/usr/bin/env python3

import sys

NUMBER2SYMBOL = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}

def hamming_distance(p, q):
    return len(list(filter(lambda x: x[0] != x[1], zip(p, q))))

def distance_between_pattern_and_strings(pattern, dna):
    k = len(pattern)
    distance = 0
    for text in dna:
        min_hamming_distance = sys.maxsize
        for i in range(len(text) - k + 1):
            pattern_in_text = text[i:i + k]
            min_hamming_distance = min(min_hamming_distance, hamming_distance(pattern, pattern_in_text))
        distance += min_hamming_distance
    return distance

def number_to_pattern(index, k):
    if k == 1:
        return NUMBER2SYMBOL[index]
    prefix_index, r = divmod(index, 4)
    prefix_pattern = number_to_pattern(prefix_index, k - 1)
    symbol = NUMBER2SYMBOL[r]
    return prefix_pattern + symbol

def median_string(dna, k):
    min_distance = sys.maxsize
    for i in range(4 ** k):
        pattern = number_to_pattern(i, k)
        distance = distance_between_pattern_and_strings(pattern, dna)
        if distance < min_distance:
            min_distance = distance
            median = pattern
    return median

def main():
    k = int(input())

    dna = []
    while True:
        try:
            dna.append(input())
        except EOFError:
            break
    
    print(median_string(dna, k))

if __name__ == '__main__':
    main()
