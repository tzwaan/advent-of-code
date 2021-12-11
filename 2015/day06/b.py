from a import make_grid, apply_function


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.read().splitlines()

    grid = make_grid(0)

    for line in lines:
        match line.split():
            case 'turn', 'on', a, 'through', b:
                apply_function(grid, a, b, lambda x: x + 1)
            case 'turn', 'off', a, 'through', b:
                apply_function(grid, a, b, lambda x: max([x - 1, 0]))
            case 'toggle', a, 'through', b:
                apply_function(grid, a, b, lambda x: x + 2)
            case _:
                raise ValueError(line)

    total_brightness = sum([
        sum(line)
        for line in grid
    ])
    print(total_brightness)

