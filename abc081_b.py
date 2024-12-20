# ruff: noqa: E731
from functools import reduce
from operator import or_
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    read()
    n = reduce(or_, mir())
    print((n & -n).bit_length() - 1)


if __name__ == "__main__":
    main()
