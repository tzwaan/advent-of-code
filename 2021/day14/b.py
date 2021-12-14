from itertools import pairwise
from a import parse_lines, score_from_counts


def count_occurances(counts):
    letter_count = {}
    for key, count in counts.items():
        a, b = key
        if a not in letter_count:
            letter_count[a] = 0
        if b not in letter_count:
            letter_count[b] = 0
        letter_count[a] += count
        letter_count[b] += count

    for key in letter_count:
        letter_count[key] //= 2
    return letter_count


def count_pairs(polymer):
    counts = {}
    for a, b in pairwise(polymer):
        if a + b not in counts:
            counts[a + b] = 0
        counts[a + b] += 1
    return counts


def apply_rules(polymer_counts, rules):
    new_counts = {}
    for key, value in polymer_counts.items():
        if key in rules:
            a, b = key
            if a + rules[key] not in new_counts:
                new_counts[a + rules[key]] = 0
            new_counts[a + rules[key]] += value
            if rules[key] + b not in new_counts:
                new_counts[rules[key] + b] = 0
            new_counts[rules[key] + b] += value
        else:
            if key not in new_counts:
                new_counts[key] = 0
            new_counts[key] += value

    return new_counts


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.read().splitlines()

    polymer, rules = parse_lines(lines)
    first, last = polymer[0], polymer[-1]
    counts = count_pairs(polymer)
    for _ in range(40):
        counts = apply_rules(counts, rules)

    counts = count_occurances(counts)
    counts[first] += 1
    counts[last] += 1

    print(score_from_counts(counts))

