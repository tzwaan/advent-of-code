from a import parse_lines, fold_grid, print_grid


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.read().splitlines()

    coordinates, folds = parse_lines(lines)

    for fold in folds:
        coordinates = fold_grid(coordinates, fold)
    print_grid(coordinates)

