class P:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __iter__(self):
        return iter((self.x, self.y))

    def neighbours(self, visited):
        height = len(visited)
        width = len(visited[0])
        if self.x > 0 and not visited[self.y][self.x - 1]:
            yield P(self.x - 1, self.y)
        if self.x + 1 < width and not visited[self.y][self.x + 2]:
            yield P(self.x + 1, self.y)
        if self.y > 0 and not visited[self.y - 1][self.x]:
            yield P(self.x, self.y - 1)
        if self.y + 1 < height and not visited[self.y + 1][self.x]:
            yield P(self.x, self.y + 1)


def dijkstra(grid):
    height = len(grid)
    width = len(grid[0])
    distances = [
        [None for _ in range(width)]
        for _ in range(height)
    ]
    visited = [
        [False for _ in range(width)]
        for _ in range(height)
    ]

    distances[0][0] = 0
    next_points = []
    cur = P(0, 0)
    while not visited[-1][-1]:
        for x, y in cur.neighbours(visited):
            distance = distances[cur.y][cur.x] + grid[y][x]
            if distances[y][x] is None or distances[y][x] > distance:
                distances[y][x] = distance
        visited[cur.y][cur.x] = True


if __name__ == '__main__':
    with open('sample_input.txt') as f:
        lines = f.read().splitlines()

    grid = [
        [int(char) for char in line]
        for line in lines
    ]

    pass
