def get_code_position(row, column):
    return sum(range(1, row + column - 1)) + column

def get_code_at(position):
    number = 20151125
    for _ in range(position - 1):
        number = (number * 252533) % 33554393
    return number


if __name__ == '__main__':
    import re

    with open('input.txt') as f:
        line = f.read()

    regex = r"To continue, please consult the code grid in the manual\.  Enter the code at row (?P<row>\d+), column (?P<column>\d+)\."

    match = re.search(regex, line)
    row = int(match.group('row'))
    column = int(match.group('column'))

    print(get_code_at(get_code_position(row, column)))

