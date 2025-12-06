import re
from functools import reduce
from operator import add, mul

with open('input.txt', 'r') as file:
    lines = [line.rstrip('\n') for line in file]

operators = lines[-1:][0]
lines = lines[:-1]

result = []
number_set = []

for l_idx in range(0, len(lines[0])):

    current_num = []
    for i in range(0, len(lines)):
        current_num.append(lines[i][l_idx])
    
    s = ("".join(current_num)).strip()

    if len(s) > 0:
        number_set.append(int(s))
    
    if len(s) == 0 or l_idx == (len(lines[0]) - 1):
        result.append(number_set)
        number_set = []

p_operators = re.compile("\\S")
operators = p_operators.findall(operators)

running_sum = 0

for idx in range(0, len(operators)):
    match operators[idx]:
        case "+": 
            running_sum += reduce(add, result[idx])
        case "*": 
            running_sum += reduce(mul, result[idx])
        case _:
            raise IndexError()

print(running_sum)