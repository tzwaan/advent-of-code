with open('input.txt') as f:
    id_ranges = f.read().split(',')

total = 0

def check_subsections(candidate_id, section_length):
    length = len(candidate_id)
    if (length % section_length != 0):
        return False;
    nr_sections = length // section_length
    section = candidate_id[:section_length]
    for i in range(1, nr_sections):
        start = i * section_length
        end = (i + 1) * section_length
        if section != candidate_id[start:end]:
            return False;
    return True;


def is_valid_id(candidate_id):
    candidate_id = str(candidate_id)
    length = len(candidate_id)
    for i in range(1, (length // 2) + 1):
        if (check_subsections(candidate_id, i)):
            return False;
    return True;

for id_range in id_ranges:
    start, end = id_range.split('-')
    start, end = int(start), int(end)
    for candidate_id in range(start, end + 1):
        if not is_valid_id(candidate_id):
            total = total + candidate_id

print(total)
