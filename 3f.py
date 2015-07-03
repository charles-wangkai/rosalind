#!/usr/bin/env python3

import collections
import functools
import itertools
import random
import sys

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

def build_motifs(profile, dna):
    return [find_profile_most_probable_k_mer(dna[i], profile) for i in range(len(dna))]

def compute_score(motifs):
    return sum(map(lambda column: len(motifs) - collections.Counter(column).most_common(1)[0][1], zip(*motifs)))

def build_profile_with_pseudocounts(motifs):
    k = len(motifs[0])
    t = len(motifs)
    columns = list(zip(*motifs))
    
    profile = [[1 / (t + 4)] * k for _ in range(4)]
    for i in range(k):
        for symbol, count in collections.Counter(collections.Counter(columns[i])).most_common():
            profile[SYMBOL2NUMBER[symbol]][i] = (count + 1) / (t + 4)
    return profile

def randomized_motif_search(dna, k, t):
    motifs = []
    for i in range(t):
        begin = random.randrange(len(dna[i]) - k + 1)
        motifs.append(dna[i][begin:begin + k])
    
    min_score = compute_score(motifs)
    best_motifs = motifs
    while True:
        profile = build_profile_with_pseudocounts(motifs)
        motifs = build_motifs(profile, dna)
        score = compute_score(motifs)
        if score < min_score:
            min_score = score
            best_motifs = motifs
        else:
            return min_score, best_motifs

def main():
    k, t = map(int, input().split())
    dna = [input() for _ in range(t)]
    
    min_score = sys.maxsize
    best_motifs = None
    for _ in range(1000):
        score, motifs = randomized_motif_search(dna, k, t)
        if score < min_score:
            min_score = score
            best_motifs = motifs
    
    print(*best_motifs, sep='\n')

if __name__ == '__main__':
    main()
