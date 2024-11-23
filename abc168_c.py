# ruff: noqa: E731
from math import cos, dist, radians, sin
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    a, b, h, m = mir()
    h = 30 * h + m / 2
    m *= 6
    print(
        dist(
            [a * cos(radians(h)), a * sin(radians(h))],
            [b * cos(radians(m)), b * sin(radians(m))],
        )
    )


if __name__ == "__main__":
    main()
