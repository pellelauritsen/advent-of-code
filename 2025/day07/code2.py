with open('input.txt', 'r') as file:
    lines = [line.rstrip('\n') for line in file]

beams = [0] * len(lines[0])

for line in lines:
    new_beams = beams[:]

    for x in range(0, len(line)):
        if line[x] == "S":
            new_beams[x] = 1

        if line[x] == "^" and beams[x] > 0:
            new_beams[x-1] += beams[x]
            new_beams[x] = 0
            new_beams[x+1] += beams[x]

    beams = new_beams

print(sum(beams))