def calc_repeating_numbers(start, end):
    values = set()

    for i in range(start, end + 1):
        num_as_str = str(i)
        len_half = len(num_as_str) // 2
        s1 = num_as_str[:len_half]
        s2 = num_as_str[len_half:]
        
        if(s1 == s2):
            values.add(int(s1+s2))

    return sum(values)

with open('input.txt', 'r') as file:
    lines = [line.rstrip('\n') for line in file]

    running_sum = 0

    for line in lines:
        for part in line.split(','):
            begin, end = map(int, part.split('-'))
            val = calc_repeating_numbers(begin, end)

            if (val):
                running_sum += val

    print("Sum:", running_sum)