brackets = {
    '}': '{',
    '>': '<',
    ')': '(',
    ']': '[',
}

reverse_brackets = {
    value: key
    for key, value in brackets.items()
}

error_score = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}


def related_bracket(bracket):
    if bracket in brackets:
        return brackets[bracket]
    else:
        return reverse_brackets[bracket]


def parse_line(line):
    stack = []

    for char in line:
        if char in '{([<':
            stack.append(char)
        else:
            opening_bracket = stack.pop()
            if opening_bracket != related_bracket(char):
                return stack, related_bracket(opening_bracket), char
    return stack, None, None


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.read().splitlines()

    total_score = 0
    for line in lines:
        _, expected, got = parse_line(line)
        if expected:
            total_score += error_score[got]
    print(total_score)

