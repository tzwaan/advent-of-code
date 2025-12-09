with open('input.txt') as f:
    id_ranges = f.read().split(',')

total = 0

def is_valid_id(candidate_id):
    candidate_id = str(candidate_id)
    length = len(candidate_id)
    if (length % 2 != 0):
        return True
    half = length // 2
    return candidate_id[:half] != candidate_id[half:]

for id_range in id_ranges:
    start, end = id_range.split('-')
    start, end = int(start), int(end)
    for candidate_id in range(start, end + 1):
        if not is_valid_id(candidate_id):
            total = total + candidate_id

print(total)


