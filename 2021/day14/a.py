from itertools import pairwise


def replace(polymer, rules):
    for a, b in pairwise(polymer):
        yield a
        if a + b in rules:
            yield rules[a + b]
    yield b


def count_occurances(polymer):
    counts = {}
    for letter in polymer:
        if letter not in counts:
            counts[letter] = 0
        counts[letter] += 1
    return counts


def parse_lines(lines):
    polymer = list(lines[0])

    rules = {
        key: value
        for key, value in [line.split(' -> ') for line in lines[2:]]
    }
    return polymer, rules


def score_from_counts(counts):
    return (
        counts[max(counts, key=counts.get)]
        - counts[min(counts, key=counts.get)]
    )



if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.read().splitlines()

    polymer, rules = parse_lines(lines)

    for _ in range(10):
        polymer = replace(polymer, rules)

    counts = count_occurances(polymer)

    print(score_from_counts(counts))

