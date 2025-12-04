EMPTY_SPACE_LIMIT = 4
EMPTY_SPACE = '.'

# paper array
a = []

with open('input.txt', 'r') as file:
    lines = [line.rstrip('\n') for line in file]

    for line in lines:
        l = [EMPTY_SPACE] + list(line) + [EMPTY_SPACE]
        a.append(l)

a.insert(0, list(EMPTY_SPACE * len(a[0])))
a.append(list(EMPTY_SPACE * len(a[0])))

width = len(a[0])
height = len(a)

rerun = False
running_sum = 0 
calc_rows = 0

# This version goes up one line, of there happend to be a change on a line
y = 1
while y < height:
    calc_rows += 1

    for x in range(1, width - 1):
        if a[y][x] == '@':
            surrounding_paper = [a[y-1][x-1],a[y-1][x],a[y-1][x+1],a[y][x-1],a[y][x+1],a[y+1][x-1],a[y+1][x],a[y+1][x+1]]
            empty_count = surrounding_paper.count(EMPTY_SPACE)

            if empty_count > EMPTY_SPACE_LIMIT:
                running_sum += 1
                a[y][x] = EMPTY_SPACE
                rerun = True
                new_y = max(1, y-1)

    y = new_y if rerun else y + 1
    rerun = False

# for y in range(0, height):
#     print(y, a[y],"\n")

print("Sum:",running_sum)
print("Calculated rows:", calc_rows)