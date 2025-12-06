is_ids = False

fresh_ranges = []
ids = []

with open('input.txt', 'r') as file:
    lines = [line.rstrip('\n') for line in file]

for line in lines:
    if not is_ids and len(line) == 0:
        is_ids = True
        continue

    if not is_ids:
        fresh_ranges.append(list(map(int, line.split("-"))))
    else:
        ids.append(int(line))

running_sum = 0

for i in ids:
    for r in fresh_ranges:
        if i >= r[0] and i <= r[1]:
            print(i,r)
            running_sum += 1
            break
        

print(running_sum)