# ruff: noqa: E731
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    s = input()
    dp = [False] * (len(s) + 1)
    dp[0] = True
    for i in range(1, len(s) + 1):
        dp[i] = (
            (i >= 5 and dp[i - 5] and s[i - 5 : i] == "dream")
            or (i >= 7 and dp[i - 7] and s[i - 7 : i] == "dreamer")
            or (i >= 5 and dp[i - 5] and s[i - 5 : i] == "erase")
            or (i >= 6 and dp[i - 6] and s[i - 6 : i] == "eraser")
        )
    print("YES" if dp[-1] else "NO")


if __name__ == "__main__":
    main()
