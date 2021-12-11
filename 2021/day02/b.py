with open('input.txt') as f:
    aim = 0
    position = 0
    depth = 0

    for line in f.readlines():
        command, amount = line.split()
        if command == 'down':
            aim += int(amount)
        elif command == 'up':
            aim -= int(amount)
        elif command == 'forward':
            position += int(amount)
            depth += aim * int(amount)

    print(position * depth)
