import collections
import fileinput
import itertools


def sort_word(word):
    return "".join(sorted(word))


def part2(lines):
    """
    Analyzing all the possible numbers we get:

           a   b   c   d   e   f   g
    -----------------------------------
      0:   x   x   x       x   x   x
      1:           x           x
      2:   x       x   x   x       x
      3:   x       x   x       x   x
      4:       x   x   x       x
      5:   x   x       x       x   x
      6:   x   x       x   x   x   x
      7:   x       x           x
      8:   x   x   x   x   x   x   x
      9:   x   x   x   x       x   x
    -----------------------------------
      r:   8   6   8   7   4   9   7    <- how many times each character is present

    If we assign each character to the value of r above, we find that each number
    can be uniquely represented by the sum of those values:

     0: abcefg = 8+6+8+4+9+7 = 42
     1: cf     = 8+9         = 17
     ... and so on
    """

    def decode(wires, output):
        counter = collections.Counter(itertools.chain(*wires))

        number = 0
        for digits in output:
            number = number * 10 + mapping[sum(counter[c] for c in digits)]
        return number

    correct = {
        0: "abcefg",
        1: "cf",
        2: "acdeg",
        3: "acdfg",
        4: "bcdf",
        5: "abdfg",
        6: "abdefg",
        7: "acf",
        8: "abcdefg",
        9: "abcdfg",
    }
    counter = collections.Counter(itertools.chain(*correct.values()))
    mapping = {sum(counter[d] for d in digits): num for num, digits in correct.items()}

    return sum(decode(*l) for l in lines)


if __name__ == "__main__":

    def parse(l):
        p1, p2 = l.split(" | ")
        return list(map(sort_word, p1.split())), list(map(sort_word, p2.split()))

    lines = [parse(l) for l in fileinput.input()]

    print("Part 1:", sum(len(v) in (2, 3, 4, 7) for _, output in lines for v in output))
    print("Part 2:", part2(lines))
