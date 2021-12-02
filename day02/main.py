import fileinput


def pilot(instructions):
    pos = 0
    depth = 0
    for cmd, amount in instructions:
        if cmd == "forward":
            pos += amount
        elif cmd == "up":
            depth -= amount
        elif cmd == "down":
            depth += amount

    return (pos, depth)


def pilot_with_aim(instructions):
    pos = 0
    depth = 0
    aim = 0
    for cmd, amount in instructions:
        if cmd == "forward":
            pos += amount
            depth += aim * amount
        elif cmd == "up":
            aim -= amount
        elif cmd == "down":
            aim += amount

    return (pos, depth)


if __name__ == "__main__":

    def parse(line):
        cmd, amount = line.split()
        return cmd, int(amount)

    instructions = list(map(parse, fileinput.input()))

    pos, depth = pilot(instructions)
    print("Part 1:", pos * depth)

    pos, depth = pilot_with_aim(instructions)
    print("Part 2:", pos * depth)
