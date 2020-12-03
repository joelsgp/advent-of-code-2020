with open('input', 'r') as input_file:
    input_raw = input_file.read()

char_map = {
    '.': False,
    '#': True
}

input_2d_list = []
for line in input_raw.splitlines():
    row_list = [char_map[char] for char in line]
    input_2d_list.append(row_list)

pass
