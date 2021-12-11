def next_array(nrs):
    new = []
    prev_nr = None
    count = 0
    for nr in nrs:
        if nr != prev_nr and count:
            new.append(count)
            new.append(prev_nr)
            count = 0
        prev_nr = nr
        count += 1
    new.append(count)
    new.append(prev_nr)
    return new


if __name__ == '__main__':
    with open('input.txt') as f:
        nrs = list(int(x) for x in f.read().strip())

    for _ in range(40):
        nrs = next_array(nrs)

    print(len(nrs))

