# ruff: noqa: E731
from collections import deque
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    n, k = mir()
    h = lmir()
    if k >= n - 1:
        print(abs(h[-1] - h[0]))
        return
    dp = deque((abs(h[i] - h[0]) for i in range(1, k + 1)), maxlen=k)
    for i in range(k + 1, n):
        mini = min(dp[-j] + abs(h[i] - h[i - j]) for j in range(1, k + 1))
        dp.append(mini)
    print(dp[-1])


if __name__ == "__main__":
    main()
