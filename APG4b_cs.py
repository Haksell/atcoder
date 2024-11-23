# ruff: noqa: E731
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    seconds = 365 * 24 * 60 * 60
    for n in (1, 2, 5, 10):
        print(n * seconds)


if __name__ == "__main__":
    main()
