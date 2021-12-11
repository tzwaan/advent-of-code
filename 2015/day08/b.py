def escape_line(_line):
    line = _line
    new_line = '"'
    i = 0
    while i < len(line):
        char = line[i]
        if char in ['\\', '"']:
            new_line += '\\' + char
            i += 1
        else:
            new_line += char
            i += 1

    return len(_line), len(new_line + '"')


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.read().splitlines()

    normal, long_ = zip(*[
        escape_line(line)
        for line in lines
    ])
    print(sum(long_) - sum(normal))

