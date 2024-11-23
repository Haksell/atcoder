# ruff: noqa: E731
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    n, c = mir()
    dp = [0] * (c + 1)
    for _ in range(n):
        w, v = mir()
        for i in range(c, w - 1, -1):
            dp[i] = max(dp[i], dp[i - w] + v)
    print(max(dp))


if __name__ == "__main__":
    main()
