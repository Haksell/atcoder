# ruff: noqa: E731
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    read()
    a = sorted(mir(), reverse=True)
    print(sum(a[::2]) - sum(a[1::2]))


if __name__ == "__main__":
    main()
