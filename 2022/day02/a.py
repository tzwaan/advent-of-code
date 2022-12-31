# A, X: Rock: 1
# B, Y: Paper: 2
# C, Z: Scissors: 3
# lose: 0
# draw: 3
# win: 6
with open('input.txt') as f:
    lines = f.read().split('\n')
    point_map = {
        "A X": 1 + 3,
        "A Y": 2 + 6,
        "A Z": 3 + 0,
        "B X": 1 + 0,
        "B Y": 2 + 3,
        "B Z": 3 + 6,
        "C X": 1 + 6,
        "C Y": 2 + 0,
        "C Z": 3 + 3,
    }

    print(sum([point_map[line] for line in lines]))
