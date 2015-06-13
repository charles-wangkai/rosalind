#!/usr/bin/env python3

SYMBOL2NUMBER = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
NUMBER2SYMBOL = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}

def number_to_pattern(index, k):
    if k == 1:
        return NUMBER2SYMBOL[index]
    prefix_index, r = divmod(index, 4)
    prefix_pattern = number_to_pattern(prefix_index, k - 1)
    symbol = NUMBER2SYMBOL[r]
    return prefix_pattern + symbol

def pattern_to_number(pattern):
    if not pattern:
        return 0
    symbol = pattern[-1]
    pattern = pattern[:-1]
    return 4 * pattern_to_number(pattern) + SYMBOL2NUMBER[symbol]

def computing_frequencies(text, k):
    frequency_array = [0] * (4 ** k)
    for i in range(len(text) - k + 1):
        pattern = text[i:i + k]
        j = pattern_to_number(pattern)
        frequency_array[j] += 1
    return frequency_array

def clump_finding(genome, k, t, L):
    frequent_patterns = set()
    clumps = [False] * (4 ** k)
    
    text = genome[:L]
    frequency_array = computing_frequencies(text, k)
    for i in range(len(frequency_array)):
        if frequency_array[i] >= t:
            clumps[i] = True
    
    for i in range(1, len(genome) - L + 1):
        first_pattern = genome[i - 1:i - 1 + k]
        j = pattern_to_number(first_pattern)
        frequency_array[j] -= 1
        
        last_pattern = genome[i + L - k:i + L]
        j = pattern_to_number(last_pattern)
        frequency_array[j] += 1
        if frequency_array[j] >= t:
            clumps[j] = True
    
    for i in range(len(clumps)):
        if clumps[i]:
            pattern = number_to_pattern(i, k)
            frequent_patterns.add(pattern)
    return frequent_patterns

def main():
    genome = input()
    k, L, t = map(int, input().split())
    print(' '.join(clump_finding(genome, k, t, L)))

if __name__ == '__main__':
    main()
