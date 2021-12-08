from a import parse_lines, print_lines


segment_mapping = [
    set((0, 1, 2, 4, 5, 6)),
    set((2, 5)),
    set((0, 2, 3, 4, 6)),
    set((0, 2, 3, 5, 6)),
    set((1, 2, 3, 5)),
    set((0, 1, 3, 5, 6)),
    set((0, 1, 3, 4, 5, 6)),
    set((0, 2, 5)),
    set((0, 1, 2, 3, 4, 5, 6)),
    set((0, 1, 2, 3, 5, 6)),
]


class Digit:
    def __init__(self, strings):
        self.__segments = [
            set('abcdefg')
            for _ in range(7)
        ]
        self.add_number_strings(strings)
        self.prune()

    def __str__(self):
        return str(self.__segments)

    def remove_chars_from_segment(self, n, string):
        for i in range(7):
            if i not in segment_mapping[n]:
                for char in string:
                    self.__segments[i].discard(char)
            else:
                for char in list(self.__segments[i]):
                    if char not in string:
                        self.__segments[i].discard(char)

    def add_number_strings(self, strings):
        sixes = []
        for string in strings:
            if len(string) in [2, 3, 4, 7]:
                self.add_number_string(string)
            elif len(string) == 6:
                sixes.append(string)
        self.add_sixes_strings(sixes)

    def add_sixes_strings(self, strings):
        for char in 'abcdefg':
            if not (
                char in strings[0]
                and char in strings[1]
                and char in strings[2]
            ):
                for i in (0, 1, 5, 6):
                    self.__segments[i].discard(char)

    def add_number_string(self, string):
        match len(string):
            case 2:
                self.remove_chars_from_segment(1, string)
            case 4:
                self.remove_chars_from_segment(4, string)
            case 3:
                self.remove_chars_from_segment(7, string)
            case 7:
                self.remove_chars_from_segment(8, string)

    def prune(self):
        for segment in self.__segments:
            if len(segment) == 1:
                char, = segment
                for _segment in self.__segments:
                    if segment is not _segment:
                        _segment.discard(char)

    @property
    def is_solved(self):
        for segment in self.__segments:
            if len(segment) > 1:
                return False
        return True

    def strings_to_number(self, strings):
        numbers = [
            self.string_to_number(string)
            for string in strings
        ]
        return int(''.join([str(x) for x in numbers]))

    def string_to_number(self, string):
        segment_numbers = set()
        for char in string:
            for i, segment in enumerate(self.__segments):
                if char in segment:
                    segment_numbers.add(i)
        for i, mapping in enumerate(segment_mapping):
            if segment_numbers == mapping:
                return i


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.read().splitlines()

    lines = parse_lines(lines)
    numbers = [
        Digit(inp).strings_to_number(out)
        for inp, out in lines
    ]
    print(sum(numbers))

