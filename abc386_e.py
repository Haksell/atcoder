# ruff: noqa: E731, E741
from functools import reduce
from operator import xor
import sys

sys.setrecursionlimit(12345)

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve(a, k):
    if k == 1:
        return max(a)
    if k == len(a):
        return reduce(xor, a)

    def dfs(x, i, k):
        if k == 0:
            return x
        return max(dfs(x ^ a[j], j + 1, k - 1) for j in range(i, len(a) - (k - 1)))

    if 2 * k <= len(a):
        return dfs(0, 0, k)
    else:
        return dfs(reduce(xor, a), 0, len(a) - k)


def main():
    _, k = mir()
    a = lmir()
    print(solve(a, k))


def test():
    pass


if __name__ == "__main__":
    if sys.stdin.isatty():
        test()
    else:
        main()
