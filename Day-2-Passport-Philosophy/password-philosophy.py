import re

with open('input', 'r') as input_file:
    input_raw = input_file.read()

input_list = input_raw.splitlines()

# example match: 1-3 a: abcde
#                ()-() (): ()
re_pattern = re.compile('([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)')

# need to extract:
# 0 lower bound
# 1 upper bound
# 2 search char
# 3 pass
# in that order

input_dicts_list = []
for input_line in input_list:
    re_match = re_pattern.match(input_line)
    input_elements = re_match.groups()

    input_dict = {
        'lower_bound': int(input_elements[0]),
        'upper_bound': int(input_elements[1]),
        'search_char': input_elements[2],
        'pass': input_elements[3]
    }
    input_dicts_list.append(input_dict)

valid_passes = 0
for input_dict in input_dicts_list:
    search_char_occurrences = input_dict['pass'].count(input_dict['search_char'])

    if input_dict['lower_bound'] <= search_char_occurrences <= input_dict['upper_bound']:
        valid_passes += 1

print(valid_passes)
