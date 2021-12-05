def parse_point(point):
    x, y = point.split(',')
    return int(x), int(y)


def parse_raw_line(raw_line):
    start, end = raw_line.split(' -> ')
    return parse_point(start), parse_point(end)


def parse_lines(lines):
    return [
        parse_raw_line(line)
        for line in lines
    ]


def is_diagonal(point_a, point_b):
    ax, ay = point_a
    bx, by = point_b
    return ax != bx and ay != by


def points_from_lines(lines):
    for line in lines:
        a, b = line
        yield a
        yield b


def get_bounding_box(lines):
    points = points_from_lines(lines)
    minx = miny = 0

    for point in points:
        if point[0] > minx:
            minx = point[0]
        if point[1] > miny:
            miny = point[1]
    return minx + 1, miny + 1


def get_direction(start, end):
    if start == end:
        return 0
    return -1 if start > end else 1


def draw_line(grid, line):
    a, b = line
    ax, ay = a
    bx, by = b
    dx, dy = get_direction(ax, bx), get_direction(ay, by)
    x, y = a
    grid[y][x] += 1
    while (x, y) != (b):
        x += dx
        y += dy
        grid[y][x] += 1


def make_grid(lines, straight_only=True):
    if straight_only:
        lines = [
            line
            for line in lines
            if not is_diagonal(*line)
        ]
    xsize, ysize = get_bounding_box(lines)
    grid = [
        [
            0 for _ in range(xsize)
        ]
        for _ in range(ysize)
    ]

    for line in lines:
        draw_line(grid, line)
    return grid


def print_grid(grid):
    for line in grid:
        for cell in line:
            if not cell:
                print('.', end='')
            else:
                print(cell, end='')
        print()


def count_intersections(grid):
    count = 0
    for line in grid:
        for cell in line:
            if cell > 1:
                count += 1
    return count



def print_lines(lines):
    for line in lines:
        print(
            f'{line[0][0]:>3},{line[0][1]:>3} -> {line[1][0]:>3},{line[1][1]:>3}'
        )


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = parse_lines(f.readlines())

    grid = make_grid(lines)
    print(count_intersections(grid))

