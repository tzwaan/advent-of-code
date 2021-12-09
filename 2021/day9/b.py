from a import (
    get_neighbour_points, get_neighbours, print_grid, read_input, get_low_points
)

def get_basin(grid, x, y):
    basin = set()
    basin.add((x, y))
    return _get_basin(grid, basin, (x, y))


def _get_basin(grid, basin, point):
    neighbours = get_neighbour_points(grid, *point)
    for x, y in neighbours:
        if (x, y) in basin:
            continue
        if grid[y][x] < 9:
            basin.add((x, y))
            basin = _get_basin(grid, basin, (x, y))
    return basin


if __name__ == '__main__':
    with open('input.txt') as f:
        grid = read_input(f.read().splitlines())

    low_points = get_low_points(grid)
    basins = sorted([
        len(get_basin(grid, *point))
        for point in low_points
    ], reverse=True)
    total = 1
    for basin in basins[:3]:
        total *= basin
    print(total)

