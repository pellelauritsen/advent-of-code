is_ids = False

fresh_ranges = []

with open('input.txt', 'r') as file:
    lines = [line.rstrip('\n') for line in file]

for line in lines:
    if len(line) == 0:
        break

    if not is_ids:
        fresh_ranges.append(list(map(int, line.split("-"))))

new_range = []
fresh_ranges.sort(key=lambda x: x[0])

for r in fresh_ranges:
    if len(new_range) == 0:
        new_range.append(r)
        continue

    should_append = True
    for nr in new_range:
        if r[0] >= nr[0] and r[1] <= nr[1]:
            # disregard as entire range is included
            print(f"Removing range: {r} because it is contained in {nr}")
            should_append = False
            break

        #Extend range
        if (r[0] < nr[1] and r[1] > nr[1]) or r[0] == nr[1]:
            #replace
            print(f"Extending range: {nr} with {r}")
            nr[1] = r[1]
            should_append = False
            break

    if should_append:
        new_range.append(r)
        print("Appending: ", r)
        should_append = False

running_sum = 0
for x in new_range:
    length = (x[1] - x[0]) + 1
    running_sum += length

print(running_sum)