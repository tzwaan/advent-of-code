# A: Rock: 1
# B: Paper: 2
# C: Scissors: 3
# X: lose: 0
# Y: draw: 3
# Z: win: 6
with open('input.txt') as f:
    lines = f.read().split('\n')
    point_map = {
        "A X": 3 + 0,
        "A Y": 1 + 3,
        "A Z": 2 + 6,
        "B X": 1 + 0,
        "B Y": 2 + 3,
        "B Z": 3 + 6,
        "C X": 2 + 0,
        "C Y": 3 + 3,
        "C Z": 1 + 6,
    }

    print(sum([point_map[line] for line in lines]))
