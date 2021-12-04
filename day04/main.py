import fileinput


def get_score(board, numbers):
    def rows_and_columns():
        yield from map(set, board)
        yield from map(set, zip(*board))

    seqs = list(rows_and_columns())

    draw = set(numbers[:4])
    for idx in range(4, len(numbers)):
        draw.add(numbers[idx])
        if any(seq <= draw for seq in seqs):
            unmarked = set().union(*board) - draw
            return idx, sum(unmarked) * numbers[idx]

    raise


if __name__ == "__main__":

    def parse(lines):
        lines = lines.splitlines()
        return [list(map(int, line.split())) for line in lines]

    blocks = "".join(fileinput.input()).split("\n\n")
    numbers = list(map(int, blocks[0].split(",")))
    boards = list(map(parse, blocks[1:]))

    scores = sorted([get_score(board, numbers) for board in boards], key=lambda b: b[0])
    print(f"Part 1: {scores[0][1]}")
    print(f"Part 2: {scores[-1][1]}")
