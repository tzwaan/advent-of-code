from a import parse_grid, step_grid


if __name__ == '__main__':
    with open('input.txt') as f:
        grid = parse_grid(f.read().splitlines())

    nr_steps = 1
    while step_grid(grid) != 100:
        nr_steps += 1

    print(nr_steps)

