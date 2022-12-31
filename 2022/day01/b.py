
with open('input.txt') as f:
    contents = f.read()
    elves = contents.split('\n\n')
    elves = [
        sum([
            int(calorie)
            for calorie in elf.split('\n')
        ])
        for elf in elves
    ]
    print(sum(sorted(elves)[-3:]))
