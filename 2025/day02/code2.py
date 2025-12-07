def recursive_check(prefix, num_as_str, length):
    if (len(num_as_str) == 0):
        return True

    if (num_as_str[0:length] == prefix):
        return recursive_check(prefix, num_as_str[length:], length)
    
    return False

def calc_repeating_numbers(start, end):
    values = set()

    for num in range(start, end + 1):
        num_as_str = str(num)

        for j in range(1, (len(num_as_str) // 2) + 1):
            prefix = num_as_str[0:j]

            if (recursive_check(prefix, num_as_str, j)):
                values.add(num)
                print("Found repeating number: ",num, " with prefix:", prefix)
                break

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