from itertools import pairwise


def is_nice(line):
    vowels = 'aeiou'
    total_vowels = 0
    for vowel in vowels:
        total_vowels += line.count(vowel)
    if total_vowels < 3:
        return False
    for a, b in pairwise(line):
        if a == b:
            break
    else:
        return False
    illegal_strings = ['ab', 'cd', 'pq', 'xy']
    for illegal_string in illegal_strings:
        if illegal_string in line:
            return False
    return True


with open('input.txt') as f:
    lines = f.readlines()

nice_lines = list(filter(
    lambda line: is_nice(line),
    lines,
))
print(len(nice_lines))

