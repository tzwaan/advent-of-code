import pathlib
import datetime
import aocd


for year in range(2015, datetime.datetime.now().year + 1):
    for day in range(1, 26):
        folder = f'{year}/day{day}'
        pathlib.Path(folder).mkdir(parents=True, exist_ok=True)
        with open(f'{folder}/input.txt', mode='w') as input_file:
            try:
                data = aocd.get_data(day=day, year=year)
                input_file.write(data)
            except aocd.exceptions.PuzzleLockedError:
                pass

