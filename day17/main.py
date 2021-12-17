import itertools


def valid(v, target):
    x, y = 0, 0
    vx, vy = v
    (x_lo, x_hi), (y_lo, y_hi) = target

    while True:
        x, y = x + vx, y + vy
        vx, vy = max(0, vx - 1), vy - 1

        if x_lo <= x <= x_hi and y_lo <= y <= y_hi:
            return True

        if (vx == 0 and x < x_lo) or x > x_hi or (vy < 0 and y < y_lo):
            return False


if __name__ == "__main__":
    target = ((217, 240), (-126, -69))

    # For part 1 we want the maximum possible vy. Since target is completely
    # below y = 0 we have that for an initial vy > 0, the probe reaches y = 0
    # with velocity -vy (and next velocity will be -vy - 1).
    # This means that the maximum possible velocity for when it reaches y = 0 is
    # -(abs(y_lo) - 1), and so the launch velocity is at most (abs(y_lo) - 1).
    # maximum height is simply the sum of vy + (vy - 1) + (vy - 2) + ... + 3 + 2 + 1
    print("Part 1:", (125 + 1) * 125 // 2)

    print(
        "Part 2:",
        sum(
            1
            for vx, vy in itertools.product(
                range(241),  # min vx is 21, but this is already fast enough
                range(-126, 127),
            )
            if valid((vx, vy), target)
        ),
    )
