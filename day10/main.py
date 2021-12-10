import fileinput
import typing

PAIRS = {"(": ")", "[": "]", "{": "}", "<": ">"}


def error_score(line):
    ERROR_SCORE = {")": 3, "]": 57, "}": 1197, ">": 25137}
    stack = []
    for token in line:
        if token in PAIRS:
            stack.append(token)
        elif token != PAIRS[stack.pop()]:
            return ERROR_SCORE[token]
    return 0


def completion_score(line):
    COMPLETION_SCORE = {")": 1, "]": 2, "}": 3, ">": 4}
    stack = []
    for token in line:
        if token in PAIRS:
            stack.append(token)
        elif token != PAIRS[stack.pop()]:
            return 0

    score = 0
    while stack:
        token = PAIRS[stack.pop()]
        score = score * 5 + COMPLETION_SCORE[token]
    return score


if __name__ == "__main__":
    lines = [l.strip() for l in fileinput.input()]

    print("Part 1:", sum(map(error_score, lines)))

    completion_scores = sorted(
        filter(None, map(completion_score, lines))
    )
    print("Part 2:", completion_scores[len(completion_scores) // 2])
