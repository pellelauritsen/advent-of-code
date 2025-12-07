with open('sample.txt', 'r') as file:
    lines = [line.rstrip('\n') for line in file]

running_sum = 0

beams = [False] * len(lines[0])

for line in lines:
    new_beams = beams
    for x in range(0, len(line)):
        if line[x] == "S":
            new_beams[x] = True

        if line[x] == "^" and beams[x]:
            new_beams[x-1] = True
            new_beams[x] = False
            new_beams[x+1] = True
            
            running_sum += 1
    beams = new_beams

print(running_sum)