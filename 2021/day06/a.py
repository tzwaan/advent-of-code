def parse_fishes(ages):
    fish_array = [0 for _ in range(9)]
    for age in ages:
        fish_array[int(age)] += 1
    return fish_array


def step(fishes):
    nr_birth = fishes[0]
    fishes = fishes[1:] + [nr_birth]
    fishes[6] += nr_birth
    return fishes


if __name__ == '__main__':
    with open('input.txt') as f:
        ages = f.read().split(',')

    fishes = parse_fishes(ages)
    for day in range(80):
        fishes = step(fishes)

    print(sum(fishes))

