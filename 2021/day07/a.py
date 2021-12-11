def fuel_for_position(buckets, position):
    total_fuel = 0
    for key, value in buckets.items():
        total_fuel += abs(position - key) * value
    return total_fuel


def make_buckets(crabs):
    buckets = {}
    for crab in crabs:
        if crab not in buckets:
            buckets[crab] = 1
        else:
            buckets[crab] += 1
    return buckets


def get_fuels(buckets, func):
    small, big = min(buckets), max(buckets)
    fuel = [
        func(buckets, i)
        for i in range(small, big+1)
    ]
    return fuel


if __name__ == '__main__':
    with open('input.txt') as f:
        crabs = f.read().split(',')

    crabs = [int(crab) for crab in crabs]
    buckets = make_buckets(crabs)
    fuel = get_fuels(buckets, fuel_for_position)
    print(min(fuel))

