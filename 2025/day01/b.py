current = 50
count = 0

with open('input.txt') as f:
    instructions = f.read().splitlines()

for instruction in instructions:
    rotate = int(instruction[1:])

    if (instruction[0] == 'R'):
        current = current + rotate
        while (current > 99):
            current = current - 100
            count = count + 1
    else:
        current = current - rotate
        while (current < 0):
            current = current + 100
            count = count + 1

print(count)

