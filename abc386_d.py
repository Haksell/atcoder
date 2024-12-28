# ruff: noqa: E731, E741
from collections import defaultdict
from itertools import chain
from random import randint
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def check(n, xs):
    black = n
    for _, v in sorted(xs.items()):
        for y, c in sorted(v):
            if c == "B":
                if y > black:
                    return False
            else:
                black = min(black, y - 1)
    return True


def main():
    f = randint(1 << 29, 1 << 30)
    n, m = mir()
    xs = defaultdict(list)
    ys = defaultdict(list)
    for _ in range(m):
        x, y, c = input().split()
        x = int(x)
        y = int(y)
        xs[x + f].append((y, c))
        ys[y + f].append((x, c))
    print("Yes" if check(n, xs) and check(n, ys) else "No")


def test():
    pass


if __name__ == "__main__":
    if sys.stdin.isatty():
        test()
    else:
        main()
