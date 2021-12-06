with open('input.txt') as f:
    instructions = f.read()

x = y = 0
visited = set()
visited.add((x, y))
for instruction in instructions:
    match instruction:
        case "v":
            y -= 1
        case ">":
            x += 1
        case "<":
            x -= 1
        case "^":
            y += 1
    visited.add((x, y))

print(len(visited))

