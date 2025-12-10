
class Grid:
    def __init__(self, grid):
        self.width = len(grid[0])
        self.height = len(grid)
        self.grid = [list(line) for line in grid]

    def has_roll(self, x, y):
        if x < 0 or x >= self.width:
            return False
        if y < 0 or y >= self.height:
            return False
        return self.grid[y][x] == '@'

    def count_neighbors(self, x, y):
        count = 0
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if i == 0 and j == 0:
                    continue
                if (self.has_roll(x + i, y + j)):
                    count += 1
        return count

    def mark_removable(self):
        self.grid = [
            [
                'x' if (
                    self.grid[y][x] == '@'
                    and self.count_neighbors(x, y) < 4
                ) else self.grid[y][x]
                for x, roll in enumerate(line)
            ]
            for y, line in enumerate(self.grid)
        ]

    def remove_and_count_marked(self):
        count = 0
        for x in range(self.width):
            for y in range(self.height):
                if self.grid[y][x] == 'x':
                    count += 1
                    self.grid[y][x] = '.'
        return count

    def print(self):
        for line in self.grid:
            print("".join(line))

    def mark_and_remove(self):
        self.mark_removable()
        return self.remove_and_count_marked()


