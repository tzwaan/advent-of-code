from itertools import pairwise, tee


def triplewise(iterable):
    a, b, c = tee(iterable, 3)
    next(b, None)
    next(c, None)
    next(c, None)
    return zip(a, b, c)


def is_nice(line):
    for a, b in pairwise(line):
        if line.count(a+b) > 1:
            break
    else:
        return False
    for a, b, c in triplewise(line):
        if a == c:
            break
    else:
        return False
    return True


with open('input.txt') as f:
    lines = f.readlines()

nice_lines = list(filter(
    lambda line: is_nice(line),
    lines,
))
print(len(nice_lines))

