def iterate_by_three(inputs):
    prev1 = inputs[0]
    current = inputs[1]
    index = 2
    total = len(inputs)
    while index < total:
        prev2, prev1, current = prev1, current, inputs[index]
        yield int(prev2), int(prev1), int(current)
        index += 1


with open('input.txt') as f:
    nr_increases = -1
    previous_number = 0
    for line in iterate_by_three(f.readlines()):
        line = sum(line)
        if line > previous_number:
            nr_increases += 1
        previous_number = line
    print(nr_increases)
