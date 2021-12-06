import hashlib


def advent_coin_hash(secret_key, nr_zeros):
    zeros = '0' * nr_zeros
    result = ''
    number = 0
    while not result.startswith(zeros):
        number += 1
        result = hashlib.md5(f'{secret_key}{number}'.encode()).hexdigest()
    return number, result


if __name__ == '__main__':
    with open('input.txt') as f:
        secret_key = f.read()
    number, result = advent_coin_hash(secret_key, 5)
    print(number, result)

