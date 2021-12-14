import collections
import fileinput


def run(templ, rules, steps):
    pairs = collections.Counter(map("".join, zip(templ, templ[1:])))
    counter = collections.Counter(templ)

    for _ in range(steps):
        for pair, count in list(pairs.items()):
            if count == 0:
                continue
            ins = rules[pair]
            pairs[pair] -= count
            pairs[pair[0] + ins] += count
            pairs[ins + pair[1]] += count
            counter[ins] += count

    counts = sorted(counter.values())
    return counts[-1] - counts[0]


if __name__ == "__main__":

    def parse(lines):
        templ_block, rules_block = "".join(lines).split("\n\n")
        rules = dict(rule.split(" -> ") for rule in rules_block.splitlines())
        return templ_block.strip(), rules

    templ, rules = parse(fileinput.input())

    print("Part 1:", run(templ, rules, 10))
    print("Part 2:", run(templ, rules, 40))
