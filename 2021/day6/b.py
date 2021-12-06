from a import parse_fishes, step


if __name__ == '__main__':
    with open('input.txt') as f:
        ages = f.read().split(',')

    fishes = parse_fishes(ages)
    for day in range(256):
        fishes = step(fishes)

    print(sum(fishes))

