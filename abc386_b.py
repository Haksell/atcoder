# ruff: noqa: E731, E741
from itertools import groupby
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
    s = input()
    r = 0
    for k, v in groupby(s):
        v = len(list(v))
        if k == "0":
            r += v // 2 + v % 2
        else:
            r += v
    print(r)


def test():
    pass


if __name__ == "__main__":
    if sys.stdin.isatty():
        test()
    else:
        main()
