output = []
for line in open("input.txt"):
    output.append([int(i) for i in line.split(",")])


def md(a, b):
    dist = 0
    for i in range(len(a)):
        dist += abs(a[i] - b[i])

    return dist


constellations = [[output.pop()]]

while output:
    need_new = True
    for i in constellations:
        for j in i:
            k = 0
            while k < len(output):
                if md(j, output[k]) <= 3:
                    i.append(output.pop(k))
                    need_new = False
                k += 1
    if need_new and output:
        constellations.append([output.pop()])

print(len(constellations))
