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
    wv = [lmir() for _ in range(n)]
    max_score = sum(v for _, v in wv)
    dp = [c + 1] * (max_score + 1)
    dp[0] = 0
    for w, v in wv:
        for i in range(max_score, v - 1, -1):
            dp[i] = min(dp[i], dp[i - v] + w)
    print(next(i for i in range(max_score, -1, -1) if dp[i] <= c))


if __name__ == "__main__":
    main()
