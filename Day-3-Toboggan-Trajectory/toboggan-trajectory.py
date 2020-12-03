with open('input', 'r') as input_file:
    input_raw = input_file.read()

slopes = [
    [1, 1],
    [3, 1],  # original
    [5, 1],
    [7, 1],
    [1, 2],
]

char_map = {
    '.': False,
    '#': True
}

input_2d_list = []
for line in input_raw.splitlines():
    row_list = [char_map[char] for char in line]
    input_2d_list.append(row_list)

all_slopes_product = 1
for slope in slopes:
    x_coord = 0
    tree_collisions = 0
    for y_coord in range(0, len(input_2d_list), slope[1]):
        input_line = input_2d_list[y_coord]

        if x_coord >= len(input_line):
            x_coord -= len(input_line)

        if input_line[x_coord]:
            tree_collisions += 1

        x_coord += slope[0]

    print(tree_collisions)
    all_slopes_product *= tree_collisions

print(all_slopes_product)
