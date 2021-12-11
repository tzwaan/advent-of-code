from a import advent_coin_hash


if __name__ == '__main__':
    with open('input.txt') as f:
        secret_key = f.read()
    number, result = advent_coin_hash(secret_key, 6)
    print(number, result)

