#!/usr/bin/env python3

def find_lengths_for_min_skew(genome):
    min_skew = 0
    lengths = [0]
    skew = 0
    for i in range(len(genome)):
        if genome[i] == 'G':
            skew += 1
        elif genome[i] == 'C':
            skew -= 1
        
        if skew < min_skew:
            min_skew = skew
            lengths = [i + 1]
        elif skew == min_skew:
            lengths.append(i + 1)
    return lengths

def main():
    genome = input()
    print(*find_lengths_for_min_skew(genome))

if __name__ == '__main__':
    main()
