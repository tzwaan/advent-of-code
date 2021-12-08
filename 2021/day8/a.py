def parse_line(line):
    inp, out = line.split(' | ')
    inp = inp.split()
    out = out.split()
    return inp, out


def parse_lines(lines):
    return [parse_line(line) for line in lines]


def print_lines(lines):
    for inp, out in lines:
        print(' '.join(inp), '|', ' '.join(out))


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.read().splitlines()

    lines = parse_lines(lines)

    nr_unique = 0
    for inp, out in lines:
        for disp in out:
            if len(disp) in [2, 4, 3, 7]:
                nr_unique += 1

    print(nr_unique)

