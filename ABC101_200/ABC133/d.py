# https://atcoder.jp/contests/abc133/tasks/abc133_d
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    n = int(input())
    a = tuple(map(int, input().split()))
    ans = [0] * n

    ans[0] = sum(a) - 2 * sum(a[1::2])
    for i in range(1, n):
        ans[i] = 2 * a[i-1] - ans[i-1]
    print(*ans)

if __name__ == '__main__':
    main()
