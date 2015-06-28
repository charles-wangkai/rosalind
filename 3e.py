#!/usr/bin/env python3

import collections
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

def score(motifs):
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

def greedy_motif_search_with_pseudocounts(dna, k, t):
    best_motifs = [dna[i][:k] for i in range(len(dna))]
    for i in range(len(dna[0]) - k + 1):
        motifs = [dna[0][i:i + k]]
        for j in range(1, t):
            profile = build_profile_with_pseudocounts(motifs)
            motifs.append(find_profile_most_probable_k_mer(dna[j], profile))
            
        if score(motifs) < score(best_motifs):
            best_motifs = motifs
    return best_motifs

def main():
    k, t = map(int, input().split())

    dna = []
    while True:
        try:
            dna.append(input())
        except EOFError:
            break

    print(*greedy_motif_search_with_pseudocounts(dna, k, t), sep='\n')

if __name__ == '__main__':
    main()
