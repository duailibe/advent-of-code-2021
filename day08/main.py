import fileinput
import itertools


def sort_word(word):
    return "".join(sorted(word))


def filter_len(values, size):
    if isinstance(size, int):
        size = [size]
    return filter(lambda d: len(d) in size, values)


def solve_letters(values):
    by_len = {
        l: list(vs) for l, vs in itertools.groupby(sorted(values, key=len), key=len)
    }
    # 1
    cf = set(by_len[2][0])
    # 7
    acf = set(by_len[3][0])

    a = acf - cf

    # 6
    abdefg = set(next(v for v in by_len[6] if not cf.issubset(v)))
    c = acf - abdefg
    f = cf - c

    adg = set(by_len[5][0]).intersection(*by_len[5])

    # 9
    abcdfg = set(next(v for v in by_len[6] if set(v) != abdefg and adg < set(v)))
    b = abcdfg - adg - acf

    # 4
    bcdf = set(by_len[4][0])
    d = bcdf - cf - b
    g = adg - a - d

    e = abdefg - adg - b - f

    return tuple(map(lambda c: list(c)[0], (a, b, c, d, e, f, g)))


def solve(wires, output):
    a, b, c, d, e, f, g = solve_letters(set(wires))
    numbers = {
        sort_word(a + b + c + e + f + g): 0,
        sort_word(c + f): 1,
        sort_word(a + c + d + e + g): 2,
        sort_word(a + c + d + f + g): 3,
        sort_word(b + c + d + f): 4,
        sort_word(a + b + d + f + g): 5,
        sort_word(a + b + d + e + f + g): 6,
        sort_word(a + c + f): 7,
        "abcdefg": 8,
        sort_word(a + b + c + d + f + g): 9,
    }
    result = 0
    for number in output:
        result = result * 10 + numbers[number]
    return result


if __name__ == "__main__":

    def parse(l):
        p1, p2 = l.split(" | ")
        return list(map(sort_word, p1.split())), list(map(sort_word, p2.split()))

    lines = [parse(l) for l in fileinput.input()]

    print("Part 1:", sum(len(v) in (2, 3, 4, 7) for _, output in lines for v in output))
    print("Part 2:", sum(solve(*l) for l in lines))
