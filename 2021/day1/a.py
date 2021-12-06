with open('input.txt') as f:
    nr_increases = -1
    previous_number = 0
    for line in f.readlines():
        line = int(line)
        if line > previous_number:
            nr_increases += 1
        previous_number = line
    print(nr_increases)
