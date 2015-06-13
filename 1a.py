#!/usr/bin/env python3

def pattern_count(text, pattern):
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i + len(pattern)] == pattern:
            count += 1
    return count

def frequent_words(text, k):
    frequent_patterns = set()
    counts = []
    for i in range(len(text) - k + 1):
        pattern = text[i:i + k]
        counts.append(pattern_count(text, pattern))
    max_count = max(counts)
    for i in range(len(text) - k + 1):
        if counts[i] == max_count:
            frequent_patterns.add(text[i:i + k])
    return frequent_patterns

def main():
    text = input()
    k = int(input())
    print(' '.join(frequent_words(text, k)))

if __name__ == '__main__':
    main()
