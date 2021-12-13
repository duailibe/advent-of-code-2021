import fileinput
import re


def fold(dots, folds):
    for fx, fy in folds:
        dots = set((abs(fx - abs(fx - x)), abs(fy - abs(fy - y))) for x, y in dots)
    return dots


def print_dots(dots):
    w = max(x for x, _ in dots) + 1
    h = max(y for _, y in dots) + 1
    for y in range(h):
        print("".join(("#" if (x, y) in dots else " ") for x in range(w)))


if __name__ == "__main__":

    def parse(lines):
        dots_lines, instr_lines = "".join(lines).split("\n\n")
        dots = [tuple(map(int, l.split(","))) for l in dots_lines.splitlines()]
        folds = []
        for line in instr_lines.splitlines():
            axis, unit = re.findall(r"^fold along ([xy])=(\d+)$", line)[0]
            if axis == "x":
                folds.append((int(unit), 0))
            else:
                folds.append((0, int(unit)))
        return dots, folds

    dots, folds = parse(fileinput.input())

    print("Part 1:", len(fold(dots, [folds[0]])))

    print("Part 2:")
    print_dots(fold(dots, folds))
