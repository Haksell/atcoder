# ruff: noqa: E731, E741
from functools import cache
from itertools import product
from random import choices, randint, seed
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))

MOD = 998244353


def naive(n, k, s):
    def good(s):
        res = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                a = sum(c == "A" for c in s[i:j])
                b = sum(c == "B" for c in s[i:j])
                c = sum(c == "C" for c in s[i:j])
                res += a & 1 == b & 1 == c & 1
        return res

    s = list(s)
    qs = [i for i, c in enumerate(s) if c == "?"]
    res = 0
    for p in product("ABC", repeat=len(qs)):
        for i, c in zip(qs, p):
            s[i] = c
        res += good(s) >= k
    return res


def smart(n, k, s):
    @cache
    def helper(i, parities, score):
        x000, x001, x010, x011, x100, x101, x110, x111 = parities
        score += x000 + x111
        if i == n:
            return int(score >= k)
        xa = (x100, x101, x110, x111, 1 + x000, x001, x010, x011)
        xb = (x010, x011, 1 + x000, x001, x110, x111, x100, x101)
        xc = (x001, 1 + x000, x011, x010, x101, x100, x111, x110)
        if s[i] == "A":
            return helper(i + 1, xa, score)
        if s[i] == "B":
            return helper(i + 1, xb, score)
        if s[i] == "C":
            return helper(i + 1, xc, score)
        return (
            helper(i + 1, xa, score)
            + helper(i + 1, xb, score)
            + helper(i + 1, xc, score)
        ) % MOD

    return helper(0, (0, 0, 0, 0, 0, 0, 0, 0), 0)


def genius(n, k, s):
    @cache
    def helper(i, parities, score):
        ss, sd, ds, dd = parities
        score += ss
        if i == n:
            return int(score >= k)
        xa = (dd, ds, sd, ss + 1)
        xb = (ds, dd, ss + 1, sd)
        xc = (sd, ss + 1, dd, ds)
        if s[i] == "A":
            return helper(i + 1, xa, score)
        if s[i] == "B":
            return helper(i + 1, xb, score)
        if s[i] == "C":
            return helper(i + 1, xc, score)
        return (
            helper(i + 1, xa, score)
            + helper(i + 1, xb, score)
            + helper(i + 1, xc, score)
        ) % MOD

    return helper(0, (0, 0, 0, 0), 0)


def main():
    if False:
        seed(42)
        for test in range(1000):
            n = randint(1, 9)
            k = randint(0, n * (n + 1) // 2)
            s = choices("ABC?", k=n)
            res_n = naive(n, k, s)
            res_s = smart(n, k, s)
            res_g = genius(n, k, s)
            if not (res_n == res_s == res_g):
                print(test, n, k, s, res_n, res_s, res_g)
                return
        return
    n, k = mir()
    s = input()
    print(genius(n, k, s))


if __name__ == "__main__":
    main()
