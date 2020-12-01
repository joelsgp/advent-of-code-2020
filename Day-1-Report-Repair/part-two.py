with open('input', 'r') as input_file:
    input_raw = input_file.read()

input_list = [int(input_str) for input_str in input_raw.split()]

for i in range(len(input_list)):
    for j in range(len(input_list)):
        for k in range(len(input_list)):
            if i == j or i == k or j ==k:
                continue
            else:
                if input_list[i]+input_list[j]+input_list[k] == 2020:
                    solution = input_list[i] * input_list[j] * input_list[k]

                    print(i)
                    print(j)
                    print(k)
                    print(input_list[i])
                    print(input_list[j])
                    print(input_list[k])
                    print(f'product: {solution}')
