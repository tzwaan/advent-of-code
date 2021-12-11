if __name__ == '__main__':
    with open('input.txt') as f:
        nrs = list(int(x) for x in f.read().strip())

    for _ in range(50):
        nrs = next_array(nrs)

    print(len(nrs))

