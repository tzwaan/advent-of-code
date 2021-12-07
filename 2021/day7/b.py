from a import make_buckets, get_fuels


def fuel_for_position(buckets, position):
    total_fuel = 0
    for key, value in buckets.items():
        pos = abs(position - key)
        total_fuel += value * pos * (pos + 1) // 2
    return total_fuel


if __name__ == '__main__':
    with open('input.txt') as f:
        crabs = f.read().split(',')

    crabs = [int(crab) for crab in crabs]
    buckets = make_buckets(crabs)
    fuel = get_fuels(buckets, fuel_for_position)
    print(min(fuel))

