with open('input', 'r') as input_file:
    input_raw = input_file.read()

groups = [group.splitlines() for group in input_raw.split('\n\n')]


def get_unique_answers(group):
    unique_answers = []
    for response in group:
        for char in response:
            if char not in unique_answers:
                unique_answers.append(char)

    return len(unique_answers)


total_counts = 0
for group in groups:
    total_counts += get_unique_answers(group)

print(total_counts)
