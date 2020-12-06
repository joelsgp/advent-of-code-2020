with open('input', 'r') as input_file:
    input_raw = input_file.read()

partitions = input_raw.splitlines()


def binary_space_partition(partition, lower_bound, upper_bound, lower_char, upper_char):
    available = [i for i in range(lower_bound, upper_bound+1)]

    for char in partition:
        split = int(len(available) / 2)

        if char == lower_char:
            available = available[split:]
        elif char == upper_char:
            available = available[:split]
        else:
            raise TypeError(f'Invalid split indicator character: {char}')

    position = available[0]
    return position


def seat_id_from_partition(partition):
    row = binary_space_partition(partition[:7], 0, 127, 'B', 'F')
    column = binary_space_partition(partition[7:], 0, 7, 'R', 'L')

    seat_id = (row * 8) + column
    return seat_id


highest_id = 0
for seat_partition in partitions:
    partition_seat_id = seat_id_from_partition(seat_partition)
    if partition_seat_id > highest_id:
        highest_id = partition_seat_id

print(highest_id)
