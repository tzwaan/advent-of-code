from joltage import calc_joltage

with open('input.txt') as f:
    banks = f.read().splitlines()

total_joltage = 0

for bank in banks:
    joltage = calc_joltage(bank, 12)
    total_joltage = total_joltage + joltage

print(total_joltage)

