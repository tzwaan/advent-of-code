def array_to_number(array):
    return int(''.join(str(i) for i in array), 2)

with open('input.txt') as f:
    lines = f.readlines()

nr_lines = len(lines)
line_length = len(lines[0].strip())
counters = [0] * line_length
for line in lines:
    for i, char in enumerate(line.strip()):
        if char == '1':
            counters[i] += 1

gamma_rate = [
    1 if counter > nr_lines / 2 else 0
    for counter in counters
]
epsilon_rate = list(map(lambda x: [1, 0][x], gamma_rate))
power_consumption = array_to_number(gamma_rate) * array_to_number(epsilon_rate)
print(power_consumption)
