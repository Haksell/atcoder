# ruff: noqa: E731
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    t = x = y = 0
    for _ in rir():
        nt, nx, ny = mir()
        dt = nt - t
        dist = abs(x - nx) + abs(y - ny)
        if dt < dist or dt & 1 != dist & 1:
            print("No")
            return
        t, x, y = nt, nx, ny
    print("Yes")


if __name__ == "__main__":
    main()
