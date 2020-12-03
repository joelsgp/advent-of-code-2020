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

x_coord = 0
tree_collisions = 0
for input_line in input_2d_list:
    if x_coord > len(input_line):
        x_coord -= len(input_line)

    if input_line[x_coord]:
        tree_collisions += 1

    x_coord += 3

print(tree_collisions)
