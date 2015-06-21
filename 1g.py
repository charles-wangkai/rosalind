#!/usr/bin/env python3

SYMBOLS = ['A', 'T', 'C', 'G']

def hamming_distance(p, q):
    return len(list(filter(lambda x: x[0] != x[1], zip(p, q))))

def approximate_pattern_count(text, pattern, d):
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        if hamming_distance(text[i:i + len(pattern)], pattern) <= d:
            count += 1
    return count

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

def frequent_words_with_mismatches(text, k, d):
    patterns = set()
    for i in range(len(text) - k + 1):
        patterns.update(approximate_patterns(text[i:i + k], d))
    
    counts = {}
    for pattern in patterns:
        counts[pattern] = approximate_pattern_count(text, pattern, d)
    
    max_count = max(counts.values())
    return filter(lambda pattern: counts[pattern] == max_count, patterns)

def main():
    text = input()
    k, d = map(int, input().split())
    print(*frequent_words_with_mismatches(text, k, d))

if __name__ == '__main__':
    main()
