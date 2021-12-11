def get_neighbour_points(grid, x, y):
    ysize = len(grid)
    xsize = len(grid[0])
    if x-1 >= 0:
        yield x-1, y
    if x+1 < xsize:
        yield x+1, y
    if y-1 >= 0:
        yield x, y-1
    if y+1 < ysize:
        yield x, y+1


def get_neighbours(grid, x, y):
    for _x, _y in get_neighbour_points(grid, x, y):
        yield grid[_y][_x]


def print_grid(grid, low_points):
    for y, line in enumerate(grid):
        for x, cell in enumerate(line):
            if (x, y) in low_points:
                print(f'\033[92m{cell}\033[0m', end='')
            else:
                print(cell, end='')
        print()


def read_input(lines):
    return [
        [int(char) for char in line]
        for line in lines
    ]


def get_low_points(grid):
    low_points = set()
    risk_level = 0

    for y, line in enumerate(grid):
        for x, cell in enumerate(line):
            if not list(filter(
                lambda _cell: _cell <= cell,
                get_neighbours(grid, x, y),
            )):
                low_points.add((x, y))
    return low_points


if __name__ == '__main__':
    with open('input.txt') as f:
        grid = read_input(f.read().splitlines())

    low_points = get_low_points(grid)
    risk_level = 0
    for x, y in low_points:
        risk_level += grid[y][x] + 1
    print(risk_level)

