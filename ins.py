#!/usr/bin/env python3

def count_swap_of_insertion_sort(a):
    swap_num = 0
    for i in range(1, len(a)):
        k = i
        while k > 0 and a[k] < a[k - 1]:
            a[k - 1], a[k] = a[k], a[k - 1]
            swap_num += 1
            k -= 1
    return swap_num

def main():
    n = int(input())
    print(count_swap_of_insertion_sort(list(map(int, input().split()))))

if __name__ == '__main__':
    main()
