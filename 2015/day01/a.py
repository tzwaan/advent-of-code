with open('input.txt') as f:
    instructions = f.read()
up = instructions.count('(')
down = instructions.count(')')
print(up - down)

