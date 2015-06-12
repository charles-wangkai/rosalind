#!/usr/bin/env python3

def PatternCount(Text, Pattern):
    count = 0
    for i in range(len(Text) - len(Pattern) + 1):
        if Text[i:i + len(Pattern)] == Pattern:
            count += 1
    return count

def FrequentWords(Text, k):
    FrequentPatterns = set()
    Count = []
    for i in range(len(Text) - k + 1):
        Pattern = Text[i:i + k]
        Count.append(PatternCount(Text, Pattern))
    maxCount = max(Count)
    for i in range(len(Text) - k + 1):
        if Count[i] == maxCount:
            FrequentPatterns.add(Text[i:i + k])
    return FrequentPatterns

def main():
    Text = input()
    k = int(input())
    print(' '.join(FrequentWords(Text, k)))

if __name__ == '__main__':
    main()
