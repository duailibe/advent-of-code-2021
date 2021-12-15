import fileinput
import heapq
import itertools


def min_risk_path(riskmap, source):
    def neighbors(pos):
        x, y = pos
        for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            if (nx, ny) != (x, y) and 0 <= nx <= dest[0] and 0 <= ny <= dest[0]:
                yield (nx, ny), riskmap[nx, ny]

    dest = max(riskmap)
    computed = {source: 0}
    visited = set()

    pq = [(0, source)]
    while pq:
        _, curr = heapq.heappop(pq)
        visited.add(curr)

        for n, risk in neighbors(curr):
            if n in visited:
                continue

            n_risk = risk + computed[curr]
            if n not in computed or n_risk < computed[n]:
                computed[n] = n_risk
                heapq.heappush(pq, (n_risk, n))

    return computed[dest]


if __name__ == "__main__":

    def parse(lines):
        return dict(
            ((x, y), int(value))
            for y, line in enumerate(lines)
            for x, value in enumerate(line.strip())
        )

    riskmap = parse(fileinput.input())

    print("Part 1:", min_risk_path(riskmap, (0, 0)))

    def grow(riskmap, tiles):
        size = max(riskmap)[0] + 1
        riskmap = dict(riskmap)
        for y, x in itertools.product(range(size * tiles), repeat=2):
            if x < size:
                if y < size:
                    continue
                else:
                    riskmap[x, y] = (riskmap[x, y - size] + 1) % 10 or 1
            else:
                riskmap[x, y] = (riskmap[x - size, y] + 1) % 10 or 1

        return riskmap

    print("Part 2:", min_risk_path(grow(riskmap, 5), (0, 0)))
