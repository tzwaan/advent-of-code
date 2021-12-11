with open('input.txt') as f:
    inputs = {
        "forward": 0,
        "down": 0,
        "up": 0,
    }
    for line in f.readlines():
        command, amount = line.split()
        inputs[command] += int(amount)

    print(inputs["forward"] * (inputs["down"] - inputs["up"]))

