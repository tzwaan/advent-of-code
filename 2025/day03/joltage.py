def calc_joltage(bank, batteries_remaining):
    joltage = ""

    highest = 0
    highest_index = -1

    while batteries_remaining > 0:
        batteries_remaining -= 1
        for i in range(highest_index + 1, len(bank) - batteries_remaining):
            current = int(bank[i])
            if current > highest:
                highest = current
                highest_index = i

        joltage += str(highest)
        highest = 0

    return int(joltage)
