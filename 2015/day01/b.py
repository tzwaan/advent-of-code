with open('input.txt') as f:

    floor = 0
    nr_instructions = 0
    while floor >= 0:
        instruction = f.read(1)
        nr_instructions += 1
        if instruction == '(':
            floor += 1
        elif instruction == ')':
            floor -= 1
        else:
            raise ValueError(instruction)

    print(nr_instructions)

