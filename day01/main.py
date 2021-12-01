import fileinput


def increases(reports):
    count = 0
    for i in range(1, len(reports)):
        if reports[i] > reports[i - 1]:
            count += 1
    return count


def window_increases(reports):
    count = 0
    for i in range(3, len(reports)):
        # previous window: (reports[i - 3], reports[i - 2], reports[i - 1])
        # current window: (reports[i - 2], reports[i - 1], reports[i])
        if reports[i] > reports[i - 3]:
            count += 1
    return count


if __name__ == "__main__":
    reports = list(map(int, fileinput.input()))

    print("Part 1:", increases(reports))
    print("Part 2:", window_increases(reports))
