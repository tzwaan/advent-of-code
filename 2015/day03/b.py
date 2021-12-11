with open('input.txt') as f:
    instructions = f.read()

sx = sy = rx = ry = 0
visited = set()
visited.add((sx, sy))
for i, instruction in enumerate(instructions):
    match (instruction, i % 2):
        case "v", 0:
            sy -= 1
        case "v", 1:
            ry -= 1
        case ">", 0:
            sx += 1
        case ">", 1:
            rx += 1
        case "<", 0:
            sx -= 1
        case "<", 1:
            rx -= 1
        case "^", 0:
            sy += 1
        case "^", 1:
            ry += 1
    if i % 2 == 0:
        visited.add((sx, sy))
    else:
        visited.add((rx, ry))

print(len(visited))

