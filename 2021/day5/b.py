from a import parse_lines, make_grid, count_intersections


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = parse_lines(f.readlines())

    grid = make_grid(lines, straight_only=False)
    print(count_intersections(grid))
