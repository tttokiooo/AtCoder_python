# https://atcoder.jp/contests/abc122/tasks/abc122_a
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    b = input()
    if b == 'A':
        print('T')
    elif b == 'T':
        print('A')
    elif b == 'C':
        print('G')
    elif b== 'G':
        print('C')

if __name__ == '__main__':
    main()