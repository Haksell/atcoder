# ruff: noqa: E731
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def digit_sum(n):
    res = 0
    while n:
        n, d = divmod(n, 10)
        res += d
    return res


def main():
    n, a, b = mir()
    print(sum(i for i in range(1, n + 1) if a <= digit_sum(i) <= b))


if __name__ == "__main__":
    main()
