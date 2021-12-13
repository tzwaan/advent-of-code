def parse_lines(lines):
    coordinates = set()
    fold_lines = []
    for i, line in enumerate(lines):
        if not line:
            fold_lines = lines[i+1:]
            break
        x, y = line.split(',')
        coordinates.add((int(x), int(y)))

    folds = []
    for line in fold_lines:
        axis, amount = line[11:].split('=')
        folds.append((axis, int(amount)))

    return coordinates, folds


def fold_grid(coordinates, fold):
    axis, number = fold
    new_coordinates = set()
    if axis == 'y':
        for x, y in coordinates:
            if y > number:
                new_coordinates.add((x, number - (y - number)))
            else:
                new_coordinates.add((x, y))
    else:
        for x, y in coordinates:
            if x > number:
                new_coordinates.add((number - (x - number), y))
            else:
                new_coordinates.add((x, y))
    return new_coordinates


def get_bounding_box(coordinates):
    maxx = maxy = 0
    for x, y in coordinates:
        if x > maxx:
            maxx = x
        if y > maxy:
            maxy = y
    return maxx, maxy


def print_grid(coordinates):
    width, height = get_bounding_box(coordinates)
    for y in range(height + 1):
        for x in range(width + 1):
            if (x, y) in coordinates:
                print('#', end='')
            else:
                print('.', end='')
        print()
    print()


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.read().splitlines()

    coordinates, folds = parse_lines(lines)
    coordinates = fold_grid(coordinates, folds[0])
    print(len(coordinates))

