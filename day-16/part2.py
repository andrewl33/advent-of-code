'''
Went ahead and did it by paper

Maybe will write it programmatically?
Find unique, by slowly eliminating numbers that are already found
or only found in one set
'''


def addr(a, b, c, l):
    l[c] = l[a] + l[b]


def addi(a, b, c, l):
    l[c] = l[a] + b


def mulr(a, b, c, l):
    l[c] = l[a] * l[b]


def muli(a, b, c, l):
    l[c] = l[a] * b


def banr(a, b, c, l):
    l[c] = l[a] & l[b]


def bani(a, b, c, l):
    l[c] = l[a] & b


def borr(a, b, c, l):
    l[c] = l[a] | l[b]


def bori(a, b, c, l):
    l[c] = l[a] | b


def setr(a, b, c, l):
    l[c] = l[a]


def seti(a, b, c, l):
    l[c] = a


def gtir(a, b, c, l):
    if a > l[b]:
        l[c] = 1
    else:
        l[c] = 0


def gtri(a, b, c, l):
    if l[a] > b:
        l[c] = 1
    else:
        l[c] = 0


def gtrr(a, b, c, l):
    if l[a] > l[b]:
        l[c] = 1
    else:
        l[c] = 0


def eqir(a, b, c, l):
    if a == l[b]:
        l[c] = 1
    else:
        l[c] = 0


def eqri(a, b, c, l):
    if l[a] == b:
        l[c] = 1
    else:
        l[c] = 0


def eqrr(a, b, c, l):
    if l[a] == l[b]:
        l[c] = 1
    else:
        l[c] = 0


# get input
input_arr = []
with open("input.txt") as file:

    count = 0
    for line in file:
        line.rstrip("\n")
        line_type = count % 4

        if line_type == 0:
            l = list(line[9:len(line)-1])
            input_arr.append([int(l[0]), int(l[3]), int(l[6]), int(l[9])])
        elif line_type == 1:
            input_arr.append(
                [int(i) for i in line.split() if i != "\n" and i != ","])
        elif line_type == 2:
            l = list(line[9:len(line)-1])
            input_arr.append([int(l[0]), int(l[3]), int(l[6]), int(l[9])])
        count += 1

candidates = {k: set() for k in range(16)}

# program count
for i in range(0, len(input_arr), 3):
    in_list = input_arr[i].copy()
    opcode, a, b, c = input_arr[i+1]
    outputs = []

    addr(a, b, c, in_list)
    outputs.append(in_list.copy())
    in_list = input_arr[i].copy()

    addi(a, b, c, in_list)
    outputs.append(in_list.copy())
    in_list = input_arr[i].copy()

    mulr(a, b, c, in_list)
    outputs.append(in_list.copy())
    in_list = input_arr[i].copy()

    muli(a, b, c, in_list)
    outputs.append(in_list.copy())
    in_list = input_arr[i].copy()

    banr(a, b, c, in_list)
    outputs.append(in_list.copy())
    in_list = input_arr[i].copy()

    bani(a, b, c, in_list)
    outputs.append(in_list.copy())
    in_list = input_arr[i].copy()

    borr(a, b, c, in_list)
    outputs.append(in_list.copy())
    in_list = input_arr[i].copy()

    bori(a, b, c, in_list)
    outputs.append(in_list.copy())
    in_list = input_arr[i].copy()

    setr(a, b, c, in_list)
    outputs.append(in_list.copy())
    in_list = input_arr[i].copy()

    seti(a, b, c, in_list)
    outputs.append(in_list.copy())
    in_list = input_arr[i].copy()

    gtir(a, b, c, in_list)
    outputs.append(in_list.copy())
    in_list = input_arr[i].copy()

    gtri(a, b, c, in_list)
    outputs.append(in_list.copy())
    in_list = input_arr[i].copy()

    gtrr(a, b, c, in_list)
    outputs.append(in_list.copy())
    in_list = input_arr[i].copy()

    eqir(a, b, c, in_list)
    outputs.append(in_list.copy())
    in_list = input_arr[i].copy()

    eqri(a, b, c, in_list)
    outputs.append(in_list.copy())
    in_list = input_arr[i].copy()

    eqrr(a, b, c, in_list)
    outputs.append(in_list.copy())
    in_list = input_arr[i].copy()

    matcher = 0
    cand = 0
    for j, out_arr in enumerate(outputs):
        if out_arr == input_arr[i+2]:
            candidates[j].add(opcode)
            matcher += 1
            cand = j

print(candidates)

print("ran some manual paper and pencil")


# this is awful
fn_list = ["addr", "addi", "mulr", "muli", "banr", "bani", "borr",
           "bori", "setr", "seti", "gtir", "gtri", "gtrr", "eqir", "eqri", "eqrr"]

t = [1, 3, 2, 13, 5, 0, 6, 10, 11, 8, 15, 4, 14, 12, 7, 9]
print(sorted([(number, fn_list[i]) for i, number in enumerate(t)]))
with open("testprog.txt") as file:
    instructions = [[int(j) for j in i.split()] for i in file]

    registers = [0, 0, 0, 0]

    for instr in instructions:
        print(fn_list[t.index(instr[0])], registers, instr)
        globals()[fn_list[t.index(instr[0])]](
            instr[1], instr[2], instr[3], registers)

    print(registers)
