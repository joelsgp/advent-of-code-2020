import string


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


def get_unanimous_answers(group):
    unanimous_answers = list(string.ascii_lowercase)

    for response in group:
        for answer in unanimous_answers:
            if answer not in response:
                del unanimous_answers[unanimous_answers.find(answer)]

    return len(unanimous_answers)


total_counts_unique = 0
total_counts_unanimous = 0
for group in groups:
    total_counts_unique += get_unique_answers(group)
    total_counts_unanimous += get_unanimous_answers(group)

print(f'unique: {total_counts_unique}')
print(f'unanimous: {total_counts_unanimous}')
