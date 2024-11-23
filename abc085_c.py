# ruff: noqa: E731
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    n, y = mir()
    y //= 1000
    for c10 in range(n + 1):
        remaining = n - c10
        c5, r = divmod(y - remaining, 4)
        c1 = n - c10 - c5
        if r == 0 and c5 >= 0 and c1 >= 0:
            print(c10, c5, c1)
            return
        y -= 10
        if y < 0:
            break
    print(-1, -1, -1)


if __name__ == "__main__":
    main()
