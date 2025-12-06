import re
from functools import reduce
from operator import add, mul


with open('input.txt', 'r') as file:
    lines = [line.rstrip('\n') for line in file]

p_numbers = re.compile("\\d+")
p_operators = re.compile("\\S")

items = []
operators = []

for line in lines:
    row = p_numbers.findall(line)

    if len(row) == 0:
        operators = p_operators.findall(line)
    else:
        items.append(map(int, row))

transposed = [list(x) for x in zip(*items)]

running_sum = 0

for idx in range(0, len(operators)):
    match operators[idx]:
        case "+": 
            running_sum += reduce(add, transposed[idx])
        case "*": 
            running_sum += reduce(mul, transposed[idx])
        case _:
            raise IndexError()

print(running_sum)