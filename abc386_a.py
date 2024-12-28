# ruff: noqa: E731, E741
from collections import Counter
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve():
    pass


def main():
    c = sorted(Counter(lmir()).values())
    print("Yes" if c == [1, 3] or c == [2, 2] else "No")


def test():
    pass


if __name__ == "__main__":
    if sys.stdin.isatty():
        test()
    else:
        main()
