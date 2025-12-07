dial_size = 100
dial_init = 50

with open('input.txt', 'r') as file:
    lines = [line.rstrip('\n') for line in file]

rolling_sum = dial_init
is_zero = 0

for line in lines:
    direction, amount = line[0], line[1:]
    amount = int(amount)

    if (amount > dial_size):
        is_zero += amount // dial_size
        amount = amount % dial_size

    old_sum = rolling_sum
    rotation_amount = amount if direction == 'R' else -amount
    rolling_sum = (rolling_sum + rotation_amount) % dial_size

    if rolling_sum % dial_size == 0:
        is_zero += 1
        # print("Hit zero at line:", line)
    elif old_sum != 0:
        if direction == 'R' and (old_sum + amount) > dial_size:
            is_zero += 1
            # print("Crossed zero at line:", line)
        elif direction == 'L' and (old_sum - amount) < 0:
            is_zero += 1
            # print("Crossed zero at line:", line)

print(is_zero)









#     old_sum = rolling_sum
#     rolling_sum += amount if direction == 'R' else -amount

#     if rolling_sum % dial_size == 0:
#         is_zero += 1
#         print("Hit zero at line:", line)
#     elif sign(old_sum) != sign(rolling_sum):
#         is_zero += 1
#         print("Sign change at line:", line)

# print(is_zero)