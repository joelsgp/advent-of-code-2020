with open('input', 'r') as input_file:
    input_raw = input_file.read()

partitions = input_raw.splitlines()
# b

def seat_id_from_partition(partition):
    # TODO: implement
    return 0


highest_id = 0
for partition in partitions:
    partition_seat_id = seat_id_from_partition(partition)
    if partition_seat_id > highest_id:
        highest_id = partition_seat_id

print(highest_id)
