class Wire:
    def __init__(self, func):
        self.func = func
        self.__cache = None

    def __call__(self):
        if self.__cache is None:
            self.__cache = self.func() % 66536
        return self.__cache

    def clear_cache(self):
        self.__cache = None


def parse_line(wires, line):
    match line.split():
        case 'NOT', inp, '->', out:
            get = Wire(lambda: ~wires[inp]())
        case a, 'AND', b, '->', out if not a.isdigit():
            get = Wire(lambda: wires[a]() & wires[b]())
        case a, 'AND', b, '->', out if a.isdigit():
            get = Wire(lambda: int(a) & wires[b]())
        case a, 'OR', b, '->', out:
            get = Wire(lambda: wires[a]() | wires[b]())
        case a, 'LSHIFT', b, '->', out:
            get = Wire(lambda: wires[a]() << int(b))
        case a, 'RSHIFT', b, '->', out:
            get = Wire(lambda: wires[a]() >> int(b))
        case a, '->', out if a.isdigit():
            get = Wire(lambda: int(a))
        case a, '->', out if not a.isdigit():
            get = Wire(lambda: wires[a]())
        case _:
            raise ValueError(line)
    wires[out] = get


def parse_wires(lines):
    wires = {}
    for line in lines:
        parse_line(wires, line)
    return wires


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.read().splitlines()

    wires = parse_wires(lines)
    print(wires['a']())

