dial_size = 100
dial_init = 50

with open('input.txt', 'r') as file:
    lines = [line.rstrip('\n') for line in file]

rolling_sum = dial_init
is_zero = 0

for line in lines:
    direction, amount = line[0], line[1:]
    amount = int(amount)
    
    rolling_sum += amount if direction == 'R' else -amount
    
    # print(rolling_sum % dial_size)
    if rolling_sum % dial_size == 0:
        is_zero += 1

print(is_zero)