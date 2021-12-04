from a import conway_cubes_from_lines

if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()

    conway_cubes = conway_cubes_from_lines(lines, 4)
    conway_cubes.fast_forward(6)
    print(len(conway_cubes.living_cells))
