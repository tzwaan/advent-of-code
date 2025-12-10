from grid import Grid

with open('input.txt') as f:
    grid = Grid(list(f.read().splitlines()))

total = 0
count = 1

while count > 0:
    count = grid.mark_and_remove()
    total += count

print(total)

