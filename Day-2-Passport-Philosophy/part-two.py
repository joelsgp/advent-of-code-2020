import re


def part_two_pass_check(in_dict):
    # have to account for index not necessarily matching string length with try-catch
    try:
        lower_bound_match = in_dict['pass'][in_dict['lower_bound']] == in_dict['search_char']
        upper_bound_match = in_dict['pass'][in_dict['upper_bound']] == in_dict['search_char']
    except IndexError:
        return False

    if lower_bound_match ^ upper_bound_match:
        return True
    else:
        return False


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
    if part_two_pass_check(input_dict):
        valid_passes += 1

print(valid_passes)
