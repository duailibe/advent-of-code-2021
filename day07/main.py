import fileinput


if __name__ == "__main__":
    crabs = list(map(int, next(fileinput.input()).split(",")))
    # crabs = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]

    part1 = min(
        sum(abs(target - pos) for pos in crabs)
        for target in range(min(crabs), max(crabs))
    )
    print("Part 1:", part1)

    part2 = min(
        sum(((abs(target - pos) + 1) * abs(target - pos)) // 2 for pos in crabs)
        for target in range(min(crabs), max(crabs))
    )
    print("Part 2:", part2)
