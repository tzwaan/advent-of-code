from a import Wire, parse_wires


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.read().splitlines()

    wires = parse_wires(lines)
    a = wires['a']()
    wires['b'] = Wire(lambda: a)
    for wire in wires.values():
        wire.clear_cache()

    print(wires['a']())

