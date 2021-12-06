import fileinput
from functools import cache


def evolve_naive(fish, days):
    fish = fish[:]
    for _ in range(days):
        for i in range(len(fish)):
            if fish[i] == 0:
                fish[i] = 6
                fish.append(8)
            else:
                fish[i] = fish[i] - 1
    return len(fish)


def evolve_smart(fish, days):
    @cache
    def descendants(days, internal):
        desc = 0
        while days > internal:
            days -= internal + 1
            desc += 1 + descendants(days, 8)
            internal = 6
        return desc

    return sum(1 + descendants(days, f) for f in fish)


if __name__ == "__main__":
    fish = list(map(int, next(fileinput.input()).strip().split(",")))

    print("Part 1:", evolve_naive(fish, 80))
    # This is too slow
    # print("Part 2:", evolve_naive(fish, 256))

    # Check part 1 with smart
    assert evolve_naive(fish, 80) == evolve_smart(fish, 80)
    print("Part 2:", evolve_smart(fish, 256))
