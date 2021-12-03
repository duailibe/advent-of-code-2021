import fileinput


def most_common(lines, index):
    count1 = sum(1 for line in lines if line[index] == "1")
    return "1" if count1 > len(lines) / 2 else "0"


def invert(digit):
    return "1" if digit == "0" else "0"


def rates(lines):
    gamma = ""
    epsilon = ""
    for i in range(len(lines[0])):
        common_digit = most_common(lines, i)
        gamma += common_digit
        epsilon += invert(common_digit)

    return (gamma, epsilon)


def life_support(lines):
    oxygen = co2 = ""

    filtered = lines
    for i in range(len(lines[0])):
        digit = most_common(filtered, i)
        filtered = [item for item in filtered if item[i] == digit]
        oxygen = filtered[0]
        if len(filtered) == 1:
            break

    filtered = lines
    for i in range(len(lines[0])):
        digit = most_common(filtered, i)
        filtered = [item for item in filtered if item[i] != digit]
        co2 = filtered[0]
        if len(filtered) == 1:
            break

    return (oxygen, co2)


if __name__ == "__main__":
    lines = [l.strip() for l in fileinput.input()]

    gamma, epsilon = rates(lines)
    print("Part 1:", int(gamma, 2) * int(epsilon, 2))

    oxygen, co2 = life_support(lines)
    print("Mult:", int(oxygen, 2) * int(co2, 2))
