'''
so if I'm assuming this is right

we get an instruction pointer register
and the next instruction is housed in that

returns register 0
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
print(ip, l)

registers = [0] * 6
registers[0] = 1  # part 2
visited = set()
while -1 < registers[ip] < len(l):
    instruction = l[registers[ip]]
    globals()[instruction[0]](instruction[1],
                              instruction[2], instruction[3], registers)
    print(registers)
    if "".join([str(i) for i in registers]) not in visited:
        visited.add("".join([str(i) for i in registers]))
    else:
        print("reached final")
    registers[ip] += 1

    # uses register 4, not 0
    if registers[4] > 10000000:
        break
counter = 1
factors = []
while counter <= registers[4]:
    if registers[4] % counter == 0:
        factors.append(counter)
    counter += 1

print(sum(factors))
