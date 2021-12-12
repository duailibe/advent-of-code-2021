import collections
import fileinput


def part1(cavemap: dict[str, list[str]]) -> int:
    def count_paths(cave: str, visited: set[str]) -> int:
        if cave == "end":
            return 1

        if cave in visited:
            return 0

        if cave.islower():
            visited = visited | {cave}

        return sum(count_paths(next_cave, visited) for next_cave in cavemap[cave])

    return count_paths("start", set())


def part2(cavemap: dict[str, list[str]]):
    def count_paths(cave: str, visited: dict[str, int], visited_twice: bool = False):
        if cave == "end":
            return 1

        if cave in visited and (cave == "start" or visited_twice):
            return 0

        if cave.islower():
            visited = dict(visited, **{cave: visited.get(cave, 0) + 1})
            visited_twice = visited_twice or visited[cave] == 2

        return sum(
            count_paths(next_cave, visited, visited_twice)
            for next_cave in cavemap[cave]
        )

    return count_paths("start", {})


if __name__ == "__main__":
    cavemap = collections.defaultdict(list)
    for line in fileinput.input():
        one, other = line.strip().split("-")
        cavemap[one].append(other)
        cavemap[other].append(one)

    print("Part 1:", part1(cavemap))
    print("Part 2:", part2(cavemap))
