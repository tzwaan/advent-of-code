def strip_line(_line):
    line = _line[1:-1]
    new_line = ''
    i = 0
    while i < len(line):
        char = line[i]
        if char == '\\':
            next_char = line[i+1]
            if next_char in ['\\', '"']:
                new_line += next_char
                i += 2
            elif next_char == 'x':
                new_line += '_'
                i += 4
        else:
            new_line += char
            i += 1

    return len(_line), len(new_line)


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.read().splitlines()

    total, short = zip(*[
        strip_line(line)
        for line in lines
    ])
    print(sum(total) - sum(short))

