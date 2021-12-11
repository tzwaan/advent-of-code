GRID_SIZE = 10


def increment_all(grid):
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            grid[y][x] += 1


def get_neighbour_points(x, y):
    for _y in range(max(y-1, 0), min(y+2, GRID_SIZE)):
        for _x in range(max(x-1, 0), min(x+2, GRID_SIZE)):
            if x == _x and y == _y:
                continue
            yield _x, _y


def flash(grid):
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            if grid[y][x] > 9:
                _flash(grid, x, y)


def _flash(grid, x, y):
    grid[y][x] = 0
    for _x, _y in get_neighbour_points(x, y):
        if grid[_y][_x] != 0:
            grid[_y][_x] += 1
            if grid[_y][_x] > 9:
                _flash(grid, _x, _y)


def count_flashes(grid):
    total = 0
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            if grid[y][x] == 0:
                total += 1
    return total


def step_grid(grid):
    increment_all(grid)
    flash(grid)
    return count_flashes(grid)


def print_grid(grid):
    for line in grid:
        print(''.join(str(char) for char in line))
    print()


def parse_grid(lines):
    return [
        [int(char) for char in line]
        for line in lines
    ]



if __name__ == '__main__':
    with open('input.txt') as f:
        grid = parse_grid(f.read().splitlines())

    total_flashes = sum(
        step_grid(grid)
        for _ in range(100)
    )

    print(total_flashes)

