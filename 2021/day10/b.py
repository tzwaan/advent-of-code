from a import related_bracket, parse_line


def close_stack(stack):
    while stack:
        yield related_bracket(stack.pop())


auto_score = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.read().splitlines()

    scores = []
    for line in lines:
        stack, expected, got = parse_line(line)
        if stack and not expected:
            line_score = 0
            auto_complete = list(close_stack(stack))
            for char in auto_complete:
                line_score *= 5
                line_score += auto_score[char]
            scores.append(line_score)
    scores = sorted(scores)
    print(scores[len(scores) // 2])

