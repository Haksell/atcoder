# ruff: noqa: E731, E741
from math import gcd
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def naive(n, k):
    def sym(grid, mi):
        r = grid[mi + 1 :] + grid[:mi]
        l = (grid[mi - 1 :: -1] if mi else []) + grid[:mi:-1]
        # print(grid, mi, l, r)
        return l == r

    grid = [False] * n
    for turn in range(n):
        mi = k if turn & 1 else 0
        for i in range(n):
            if not grid[i]:
                grid[i] = True
                if sym(grid, mi):
                    break
                grid[i] = False
        else:
            # print(n, k, grid)
            return False
    return True


def smart(n, k):
    if n <= 3:
        return True
    elif n & 3 == 0:
        return False
    elif n == k << 1:
        return False
    if n & 3 == 2:
        n >>= 1

    if gcd(n, k) == 1:
        return True
    else:
        return False


def main():
    if 0:
        for n in range(2, 31):
            for k in range(1, n):
                res_n = naive(n, k)
                res_s = smart(n, k)
                # print(n, k, res_n, res_s)
                if res_n != res_s:
                    return
            # print()
        return
    for _ in rir():
        n, k = mir()
        k = min(k, n - k)
        print("Yes" if smart(n, k) else "No")


if __name__ == "__main__":
    main()

"""
0 2k -2k 4k -4k
"""
