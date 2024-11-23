# ruff: noqa: E731
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    n = ir()
    h = lmir()
    cost = [0] * n
    cost[1] = abs(h[1] - h[0])
    for i in range(2, n):
        cost[i] = min(
            cost[i - 1] + abs(h[i] - h[i - 1]), cost[i - 2] + abs(h[i] - h[i - 2])
        )
    print(cost[-1])


if __name__ == "__main__":
    main()
