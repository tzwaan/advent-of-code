class Board:
    def __init__(self, lines):
        self.__last_number = None
        self.__board = [
            [
                [int(number), False]
                for number in line.strip().split()
            ]
            for line in lines
        ]

    @staticmethod
    def __number_to_string(number):
        output = f'{number[0]:>2}'
        if number[1]:
            output = f'\033[92m{output}\033[0m'
        return output

    def __str__(self):
        output = 'board:\n'
        output += '\n'.join([
            ' '.join([
                self.__number_to_string(number)
                for number in line
            ])
            for line in self.__board
        ]) + '\n'
        if self.has_won:
            output += f'winner! Score: {self.score}\n'
        return output

    def set_number(self, number):
        self.__last_number = number
        for line in self.lines:
            for _number in line:
                if _number[0] == number:
                    _number[1] = True
                    return

    @property
    def lines(self):
        return self.__board

    @property
    def columns(self):
        return [*zip(*self.__board)]

    @property
    def diagonals(self):
        return [
            [self.__board[i][i] for i in range(5)],
            [self.__board[i][-i] for i in range(5)],
        ]

    @staticmethod
    def __check_lines(lines):
        for line in lines:
            if sum([number[1] for number in line]) == 5:
                return True
        return False

    def check_lines(self):
        return self.__check_lines(self.lines)

    def check_columns(self):
        return self.__check_lines(self.columns)

    def check_diagonals(self):
        return self.__check_lines(self.diagonals)

    @property
    def has_won(self):
        return self.check_lines() or self.check_columns() or self.check_diagonals()

    @property
    def score(self):
        if not self.has_won:
            return 0
        numbers = [
            number[0]
            for line in self.lines
            for number in line
            if not number[1]
        ]
        return sum(numbers) * (self.__last_number or 0)


def has_another_line(f):
    current_pos = f.tell()
    has_line = bool(f.readline())
    f.seek(current_pos)
    return has_line


def set_number(boards, number):
    for board in boards:
        board.set_number(number)


def check_winner(boards):
    for board in boards:
        if board.has_won:
            return board
    return None


def parse_file(filename):
    boards = []

    with open(filename) as f:
        numbers = [
            int(number)
            for number in f.readline().strip().split(',')
        ]
        while has_another_line(f):
            f.readline()
            boards.append(
                Board([f.readline().strip() for _ in range(5)])
            )

    return boards, numbers


if __name__ == '__main__':
    boards = []

    boards, numbers = parse_file('input.txt')

    while not (winner := check_winner(boards)):
        set_number(boards, numbers[0])
        numbers = numbers[1:]

    winner = check_winner(boards)
    print(winner)
