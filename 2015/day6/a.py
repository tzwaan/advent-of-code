def parse_point(point):
    a, b = point.split(',')
    return int(a), int(b)


def coordinates(a, b):
    for x in range(a[0], b[0] + 1):
        for y in range(a[1], b[1] + 1):
            yield x, y


def apply_function(grid, a, b, func):
    for x, y in coordinates(parse_point(a), parse_point(b)):
        grid[y][x] = func(grid[y][x])


def make_grid(default):
    return [
        [default for x in range(1000)]
        for y in range(1000)
    ]


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.read().splitlines()

    grid = make_grid(False)

    for line in lines:
        match line.split():
            case 'turn', 'on', a, 'through', b:
                apply_function(grid, a, b, lambda x: True)
            case 'turn', 'off', a, 'through', b:
                apply_function(grid, a, b, lambda x: False)
            case 'toggle', a, 'through', b:
                apply_function(grid, a, b, lambda x: not x)
            case _:
                raise ValueError(line)

    nr_lights_on = sum([
        sum(line)
        for line in grid
    ])
    print(nr_lights_on)

