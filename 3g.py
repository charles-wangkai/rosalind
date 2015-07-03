#!/usr/bin/env python3

import collections
import functools
import itertools
import random
import sys

SYMBOL2NUMBER = {'A': 0, 'C': 1, 'G': 2, 'T': 3}

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

def profile_randomly_generated_k_mer(text, profile):
    k = len(profile[0])
    
    probs = []
    for i in range(len(text) - k + 1):
        k_mer = text[i:i + k]
        prob = functools.reduce(lambda x, y: x * y, itertools.starmap(lambda index, symbol: profile[SYMBOL2NUMBER[symbol]][index], enumerate(k_mer)))
        probs.append(prob)
        
    prob_sum = sum(probs)
    probs = [prob / prob_sum for prob in probs]
    
    accumulated_probs = list(itertools.accumulate(probs))
    
    x = random.random()
    for i in range(len(accumulated_probs)):
        if x < accumulated_probs[i]:
            return text[i:i + k]

def gibbs_sampler(dna, k, t, n):
    motifs = []
    for i in range(t):
        begin = random.randrange(len(dna[i]) - k + 1)
        motifs.append(dna[i][begin:begin + k])

    min_score = compute_score(motifs)
    best_motifs = motifs
    for _ in range(n):
        i = random.randrange(t)
        profile = build_profile_with_pseudocounts(motifs[:i] + motifs[i + 1:])
        motifs = motifs[:i] + [profile_randomly_generated_k_mer(dna[i], profile)] + motifs[i + 1:]
        score = compute_score(motifs)
        if score < min_score:
            min_score = score
            best_motifs = motifs
    return min_score, best_motifs

def main():
    k, t, n = map(int, input().split())
    dna = [input() for _ in range(t)]
    
    min_score = sys.maxsize
    best_motifs = None
    for _ in range(20):
        score, motifs = gibbs_sampler(dna, k, t, n)
        if score < min_score:
            min_score = score
            best_motifs = motifs
    
    print(*best_motifs, sep='\n')

if __name__ == '__main__':
    main()
