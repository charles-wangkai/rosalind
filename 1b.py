#!/usr/bin/env python3

COMPLEMENTS = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

def reverse_complement(pattern):
    return ''.join(reversed(list(map(lambda x: COMPLEMENTS[x], pattern))))

def main():
    pattern = input()
    print(reverse_complement(pattern))

if __name__ == '__main__':
    main()
