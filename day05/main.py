import fileinput
from collections import Counter


def points(segment):
    (x1, y1), (x2, y2) = sorted(segment)
    if x1 == x2:
        return ((x1, y) for y in range(y1, y2 + 1))
    slope = (y2 - y1) // (x2 - x1)
    return ((x1 + dx, y1 + slope * dx) for dx in range(x2 - x1 + 1))


def count_overlaps(lines):
    counter = Counter(point for segment in lines for point in points(segment))
    return sum(v >= 2 for v in counter.values())


if __name__ == "__main__":

    def parse(line):
        start, end = line.split(" -> ")
        return tuple(map(int, start.split(","))), tuple(map(int, end.split(",")))

    lines = [parse(l) for l in fileinput.input()]

    overlaps = count_overlaps(
        filter(lambda s: s[0][0] == s[1][0] or s[0][1] == s[1][1], lines)
    )
    print("Part 1:", overlaps)
    print("Part 2:", count_overlaps(lines))
