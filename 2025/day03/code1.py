def find_jolt_numer(s):
    first_num = '0'
    second_num = '0'

    for i in range(0, len(s) - 1):
        if (s[i] > first_num):
            first_num = s[i]
            second_num = s[i+1]
        
        for j in range(i + 1, len(s)):
            if (s[j] > second_num):
                second_num = s[j]
    
    return int(first_num + second_num)

with open('input.txt', 'r') as file:
    lines = [line.rstrip('\n') for line in file]

running_sum = 0

for line in lines:
    jn = find_jolt_numer(line)
    print(f"Jolt number for line {line} is {jn}")
    running_sum += jn

print("Sum:", running_sum)