def find_jolt_number(s, length=12):
    num_value = '0'
    num_idx = 0

    for i in range(0, len(s) - length + 1):
        if s[i] > num_value:
            num_value = s[i]
            num_idx = i

            if (num_value == '9'):
                break

    return num_value + (find_jolt_number(s[num_idx + 1:], length - 1) if length > 1 else '')
    

with open('input.txt', 'r') as file:
    lines = [line.rstrip('\n') for line in file]

    running_sum = 0

    for line in lines:
        jn = find_jolt_number(line)
        print(f"Jolt number for line {line} is {jn}")
        running_sum += int(jn)

    print("Sum:", running_sum)