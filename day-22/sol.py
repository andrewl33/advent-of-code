# real
DEPTH = 4080
TARGET_X = 785
TARGET_Y = 14

# test
# DEPTH = 510
# TARGET_X = 10
# TARGET_Y = 10
# X_VAL = 16807
# Y_VAL = 48271
# MOD = 20183

cave = [[0] * (DEPTH+1) for _ in range(DEPTH+1)]

for i in range(0, DEPTH+1):
    for j in range(0, DEPTH + 1):
        if i == 0:
            cave[i][j] = (16807*j + DEPTH) % 20183
        elif j == 0:
            cave[i][j] = (48271*i + DEPTH) % 20183
        elif i == TARGET_X and j == TARGET_Y:
            cave[i][j] = DEPTH % 20183
        else:
            cave[i][j] = (cave[i-1][j] * cave[i][j-1] + DEPTH) % 20183

# printer
for i in range(len(cave[:20])):
    to_print = []
    for j in range(len(cave[0][:20])):
        if j == TARGET_Y and i == TARGET_X:
            to_print.append("T")
        elif cave[i][j] % 3 == 0:
            to_print.append(".")
        elif cave[i][j] % 3 == 1:
            to_print.append("=")
        else:
            to_print.append("|")
    print(''.join(to_print))

# count
counter = 0
for i in range(TARGET_X+1):
    for j in range(TARGET_Y+1):
        counter += cave[i][j] % 3

print(counter)


# part 2
# rocky, climbing gear or torch cannot have neither 0
# wet, climbing or neither cannot have torch 1
# narrow torch or neither cannot have climb 2
# moving costs 1 min
# swap costs 7 mins
# you start with a torch
# you need torch in goal area
# moving directions is 4
# this is dijkstra's algorithm


def valid_path(x, y, z):
    return DEPTH+2 > x and DEPTH+2 > y and x > -1 and y > -1 and z != cave[x][y] % 3


import heapq

# minutes, x, y, type of item
hq = [(0, 0, 0, 1)]
# x, y, type = minutes
visited = dict()
# for _ in range(500):
while hq:
    top = heapq.heappop(hq)
    print(top)
    # check if it is where we are supposed to be
    if top[1] == TARGET_X and top[2] == TARGET_Y and top[3] == 1:
        print(top[0])
        break

    # if there is better, skip
    if (top[1], top[2], top[3]) in visited and visited[(top[1], top[2], top[3])] <= top[0]:
        continue
    else:
        visited[(top[1], top[2], top[3])] = top[0]

    # add to queue other types of tools if valid
    for i in range(3):
        if i != top[3] and i != cave[top[1]][top[2]] % 3:
            heapq.heappush(hq, (top[0] + 7, top[1], top[2], i))

    # traverse
    if valid_path(top[1] - 1, top[2], top[3]):
        heapq.heappush(hq, (top[0]+1, top[1] - 1, top[2], top[3]))
    if valid_path(top[1] + 1, top[2], top[3]):
        heapq.heappush(hq, (top[0]+1, top[1] + 1, top[2], top[3]))
    if valid_path(top[1], top[2]-1, top[3]):
        heapq.heappush(hq, (top[0]+1, top[1], top[2] - 1, top[3]))
    if valid_path(top[1], top[2]+1, top[3]):
        heapq.heappush(hq, (top[0]+1, top[1], top[2] + 1, top[3]))
