#!/usr/bin/env python3

def hamming_distance(p, q):
    return len(list(filter(lambda x: x[0] != x[1], zip(p, q))))

def approximate_pattern_matching(pattern, genome, d):
    indices = []
    for i in range(len(genome) - len(pattern) + 1):
        if hamming_distance(genome[i:i + len(pattern)], pattern) <= d:
            indices.append(i)
    return indices

def main():
    pattern = input()
    genome = input()
    d = int(input())
    print(*approximate_pattern_matching(pattern, genome, d))

if __name__ == '__main__':
    main()
