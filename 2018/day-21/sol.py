'''
I can hear the CPU fans turning, literally takes 20-30 mins to run
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


input_arr = []

with open("input.txt") as file:
    input_arr = [i.rstrip("\n").split() for i in file]


ip = int(input_arr[0][1])
del input_arr[0]

l = []

for i in input_arr:
    l.append([i[0], int(i[1]), int(i[2]), int(i[3])])

registers = [0] * 6
repeat_set = set()
top_set = -1
g = globals()
while registers[ip] < len(l):
    instruction = l[registers[ip]]
    g[instruction[0]](instruction[1],
                      instruction[2], instruction[3], registers)
    registers[ip] += 1
    if registers[2] == 28:
        if registers[3] not in repeat_set:
            repeat_set.add(registers[3])
            top_set = registers[3]
        else:
            print(top_set)
            break
