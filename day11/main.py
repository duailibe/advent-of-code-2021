import copy
import fileinput
import itertools


def adjacents(x, y):
    for dx, dy in itertools.product(range(-1, 2), repeat=2):
        if (dx, dy) != (0, 0) and 0 <= x + dx < 10 and 0 <= y + dy < 10:
            yield x + dx, y + dy


def step(octmap):
    for x, y in itertools.product(range(10), repeat=2):
        octmap[y][x] += 1

    flashed = set()
    while True:
        flash = [
            (x, y)
            for x, y in itertools.product(range(10), repeat=2)
            if octmap[y][x] > 9
        ]
        if not flash:
            break
        for x, y in flash:
            octmap[y][x] = 0
            flashed.add((x, y))
            for nx, ny in adjacents(x, y):
                if (nx, ny) not in flashed:
                    octmap[ny][nx] += 1

    return len(flashed)

def part1(octmap):
    octmap = copy.deepcopy(octmap)
    return sum(step(octmap) for _ in range(100))

def part2(octmap):
    octmap = copy.deepcopy(octmap)
    steps = 1
    while step(octmap) != 100:
        steps += 1
    return steps


if __name__ == "__main__":
    octmap = [list(map(int, l.strip())) for l in fileinput.input()]

    print("Part 1:", part1(octmap))
    print("Part 2:", part2(octmap))
