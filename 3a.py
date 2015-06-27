#!/usr/bin/env python3

SYMBOLS = ['A', 'T', 'C', 'G']

def search_approximate_patterns(patterns, template, remain, pattern):
    if len(pattern) == len(template):
        patterns.add(pattern)
        return
    
    search_approximate_patterns(patterns, template, remain, pattern + template[len(pattern)])
    if remain:
        for symbol in SYMBOLS:
            search_approximate_patterns(patterns, template, remain - 1, pattern + symbol)

def approximate_patterns(template, d):
    patterns = set()
    search_approximate_patterns(patterns, template, d, '')
    return patterns

def hamming_distance(p, q):
    return len(list(filter(lambda x: x[0] != x[1], zip(p, q))))

def approximate_pattern_count(text, pattern, d):
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        if hamming_distance(text[i:i + len(pattern)], pattern) <= d:
            count += 1
    return count

def appear_in_each(dna, pattern, d):
    return all(map(lambda s: approximate_pattern_count(s, pattern, d) > 0, dna))

def motif_enumeration(dna, k, d):
    patterns = set()
    for i in range(len(dna[0]) - k + 1):
        pattern = dna[0][i:i + k]
        for approximate_pattern in approximate_patterns(pattern, d):
            if appear_in_each(dna, approximate_pattern, d):
                patterns.add(approximate_pattern)
    return patterns

def main():
    k, d = map(int, input().split())
    
    dna = []
    while True:
        try:
            dna.append(input())
        except EOFError:
            break
    
    print(*motif_enumeration(dna, k, d))

if __name__ == '__main__':
    main()
