with open('input.txt') as f:
    lines = f.readlines()

def get_char_count(lines, char, index):
    count = 0
    for line in lines:
        if line[index] == char:
            count += 1
    return count


def is_most_common(lines, char, index):
    half = len(lines) / 2
    count = get_char_count(lines, char, index)
    return count >= half

def is_least_common(lines, char, index):
    half = len(lines) / 2
    count = get_char_count(lines, char, index)
    return count <= half

lines = [line.strip() for line in lines]

def find_rating(lines, char, compare_func):
    line_length = len(lines[0])
    for index in range(line_length):
        if len(lines) == 1:
            break
        if compare_func(lines, char, index):
            lines = list(filter(lambda line: line[index] == char, lines))
        else:
            lines = list(filter(lambda line: line[index] != char, lines))
    return lines[0]

oxygen_generator_rating = find_rating(lines, '1', is_most_common)
co2_scrubber_rating = find_rating(lines, '0', is_least_common)
life_support_rating = int(oxygen_generator_rating, 2) * int(co2_scrubber_rating, 2)
print(life_support_rating)

