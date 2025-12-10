from grid import Grid

with open('input.txt') as f:
    grid = Grid(list(f.read().splitlines()))

total = grid.mark_and_remove()

print(total)

