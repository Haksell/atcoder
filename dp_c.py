# ruff: noqa: E731
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    la = lb = lc = 0
    for _ in rir():
        a, b, c = mir()
        la, lb, lc = a + max(lb, lc), b + max(la, lc), c + max(la, lb)
    print(max(la, lb, lc))


if __name__ == "__main__":
    main()
