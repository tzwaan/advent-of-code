import pathlib
import datetime
import aocd
from tqdm import tqdm

starting_year = 2015
current_year = datetime.datetime.now().year

total_years = starting_year - current_year + 1

for year in tqdm(
        range(starting_year, current_year + 1),
        total=total_years,
        leave=False
):
    for day in tqdm(range(1, 26), total=25, leave=False):
        try:
            data = aocd.get_data(day=day, year=year)
        except aocd.exceptions.PuzzleLockedError as e:
            tqdm.write(str(e))
            break
        folder = f'{year}/day{day:0>2}'
        pathlib.Path(folder).mkdir(parents=True, exist_ok=True)
        with open(f'{folder}/input.txt', mode='w') as input_file:
            input_file.write(data)

