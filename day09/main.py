import fileinput
import itertools
import math


def neighbors(hmap, x, y):
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if 0 <= x + dx < len(hmap[0]) and 0 <= y + dy < len(hmap):
            yield x + dx, y + dy


def lowlevels(hmap):
    for y, x in itertools.product(range(len(hmap)), range(len(hmap[0]))):
        if all(hmap[y][x] < hmap[ny][nx] for nx, ny in neighbors(hmap, x, y)):
            yield x, y, hmap[y][x]


def basin(hmap, x, y):
    result = {(x, y)}

    q = [(x, y)]
    while q:
        x, y = q.pop(0)
        for nx, ny in neighbors(hmap, x, y):
            if (
                (nx, ny) not in result
                and hmap[ny][nx] != 9
                and hmap[ny][nx] > hmap[y][x]
            ):
                result.add((nx, ny))
                q.append((nx, ny))

    return result


if __name__ == "__main__":

    def parse(line):
        return [int(i) for i in line]

    hmap = [parse(l.strip()) for l in fileinput.input()]

    print("Part 1:", sum(1 + level for _, _, level in lowlevels(hmap)))

    basins = sorted(len(basin(hmap, x, y)) for x, y, _ in lowlevels(hmap))
    print("Part 2:", math.prod(basins[-3:]))
