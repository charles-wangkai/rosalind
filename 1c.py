#!/usr/bin/env python3

def pattern_matching(pattern, genome):
    indices = []
    for i in range(len(genome) - len(pattern) + 1):
        if genome[i:i + len(pattern)] == pattern:
            indices.append(i)
    return indices

def main():
    pattern = input()
    genome = input()
    print(' '.join(map(str, pattern_matching(pattern, genome))))

if __name__ == '__main__':
    main()
