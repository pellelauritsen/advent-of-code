EMPTY_SPACE_LIMIT = 4
EMPTY_SPACE = '.'

# paper array
a = []

with open('sample.txt', 'r') as file:
    lines = [line.rstrip('\n') for line in file]

for line in lines:
    l = [EMPTY_SPACE] + list(line) + [EMPTY_SPACE]
    a.append(l)

a.insert(0, list(EMPTY_SPACE * len(a[0])))
a.append(list(EMPTY_SPACE * len(a[0])))

width = len(a[0])
height = len(a)

running_sum = 0

for y in range(1, height - 1):
    for x in range(1, width - 1):
        if a[y][x] == '@':
            surrounding_paper = [a[y-1][x-1],a[y-1][x],a[y-1][x+1],a[y][x-1],a[y][x+1],a[y+1][x-1],a[y+1][x],a[y+1][x+1]]
            empty_count = surrounding_paper.count(EMPTY_SPACE)

            if empty_count > EMPTY_SPACE_LIMIT:
                running_sum += 1
                a[y][x] = 'X'

print("Sum:",running_sum)