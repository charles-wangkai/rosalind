#!/usr/bin/env python3

def main():
    print_out = False
    while True:
        try:
            line = input()
        except EOFError:
            break
        
        if print_out:
            print(line)
        print_out = not print_out

if __name__ == '__main__':
    main()
