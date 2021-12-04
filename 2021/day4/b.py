from a import Board, set_number, check_winner, has_another_line, parse_file


def get_loser(boards, numbers):
    for number in numbers:
        set_number(boards, number)
        while winner := check_winner(boards):
            if len(boards) == 1:
                return winner
            boards.remove(winner)
    return None


if __name__ == '__main__':
    boards = []

    boards, numbers = parse_file('input.txt')

    winner = get_loser(boards, numbers)

    print(winner)
