class Cell:
    def __init__(self, *coordinates):
        self.coordinates = coordinates

    def __len__(self):
        return self.nr_dimensions

    def __repr__(self):
        return 'Cell(' + ', '.join([str(c) for c in self.coordinates]) + ')'

    def __hash__(self):
        return hash(self.coordinates)

    def __getitem__(self, index):
        return self.coordinates[index]

    def __eq__(self, other):
        return self.coordinates == other.coordinates

    @property
    def nr_dimensions(self):
        return len(self.coordinates)

    @property
    def neighbour_cells(self):
        result =  set(self.__recursive_neighbour_cells(0))
        result.remove(self)
        return result

    def __recursive_neighbour_cells(self, current_dimension, *coordinates):
        if current_dimension == self.nr_dimensions:
            yield Cell(*coordinates)
        else:
            for i in range(
                self.coordinates[current_dimension] - 1,
                self.coordinates[current_dimension] + 2
            ):
                yield from self.__recursive_neighbour_cells(
                    current_dimension + 1,
                    *coordinates,
                    i,
                )

    def is_neighbour(self, other):
        for dimension in range(self.nr_dimensions):
            if abs(self[dimension] - other[dimension]) > 1:
                return False
        return True


class ConwayCubes:
    def __init__(self, dimensions=2):
        self.__nr_dimensions = dimensions
        self.__living_cells = set()

    @property
    def nr_dimensions(self):
        return self.__nr_dimensions

    @property
    def bounding_box(self):
        results = []
        for i in range(self.nr_dimensions):
            results.append(
                min(map(lambda cell: cell[i], self.living_cells))
            )
            results.append(
                max(map(lambda cell: cell[i], self.living_cells))
            )
        return tuple(results)

    def __recursive_str(self, header, bounding_box, *coordinates):
        if len(bounding_box) == 4:
            output = header
            output += '\n'
            x_min, x_max, y_min, y_max = bounding_box
            for y in range(y_min, y_max + 1):
                for x in range(x_min, x_max + 1):
                    if self.is_alive(x, y, *coordinates):
                        output += '#'
                    else:
                        output += '.'
                output += '\n'
            output += '\n'
            return output
        else:
            dimension_name = f'dim{len(bounding_box) // 2}'
            dim_min, dim_max = bounding_box[-2:]
            output = ''
            for dimension in range(dim_min, dim_max + 1):
                _header = header + f'{dimension_name}={dimension}, '
                output += self.__recursive_str(_header, bounding_box[:-2], dimension, *coordinates)
            return output

    def __str__(self):
        bounding_box = self.bounding_box
        return self.__recursive_str('', bounding_box)

    def set_alive(self, *args):
        extra_dimensions = self.nr_dimensions - len(args)
        self.__living_cells.add(Cell(*args, *[0] * extra_dimensions))

    def is_alive(self, *args):
        return Cell(*args) in self.__living_cells

    @property
    def living_cells(self):
        return self.__living_cells

    @property
    def active_cells(self):
        active_cells = set()
        for living_cell in self.__living_cells:
            for active_cell in living_cell.neighbour_cells:
                active_cells.add(active_cell)
        return active_cells

    def get_living_neighbours(self, cell):
        cells = set(filter(
            lambda living_cell: living_cell.is_neighbour(cell),
            self.living_cells
        ))
        if cell in cells:
            cells.remove(cell)
        return cells

    def __next_state(self):
        next_state = set()
        for cell in self.active_cells:
            nr_neighbours = len(self.get_living_neighbours(cell))
            if cell in self.living_cells and nr_neighbours in (2, 3):
                next_state.add(cell)
            elif nr_neighbours == 3:
                next_state.add(cell)
        return next_state

    def next_state(self):
        self.__living_cells = self.__next_state()

    def fast_forward(self, number):
        for _ in range(number):
            self.next_state()


def conway_cubes_from_lines(lines, dimensions):
    conway_cubes = ConwayCubes(dimensions=dimensions)
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == '#':
                conway_cubes.set_alive(x, y)
    return conway_cubes


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()

    conway_cubes = conway_cubes_from_lines(lines, 3)
    conway_cubes.fast_forward(6)
    print(len(conway_cubes.living_cells))
