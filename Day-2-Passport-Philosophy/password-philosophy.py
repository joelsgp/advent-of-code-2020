import re

with open('input', 'r') as input_file:
    input_raw = input_file.read()

input_list = input_raw.split()

re_pattern = ''
re_pattern_object = re.compile(re_pattern)

# need to extract:
# 0 lower bound
# 1 upper bound
# 2 search char
# 3 pass
# in that order

for input_line in input_list:
    re_match = re_pattern_object.match(input_line)
    input_elements_list = re_match.groups()

valid_passes = 0
for elements in input_elements_list:
    search_char_occurrences = elements[3].count(elements[2])

    if elements[0] <= search_char_occurrences <= elements[1]:
        valid_passes += 1

print(valid_passes)
