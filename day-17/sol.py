'''
water spout at x=500, y = 0

first number is the line it lives on
second range is the amount of clay

Water fills buckets, but is not affected by water pressure

can overflow though

range is in minimum Y val to greatest Y val

y is the i
x is the j
'''

import re
from collections import deque
# process input
in_arr = []

with open("test.txt") as file:
    in_arr = [sorted([i.rstrip(",") for i in l.split()]) for l in file]

flats = []
verticals = []

for itm in in_arr:
    i = [j[2:] for j in itm]
    item = []
    if bool(re.search(r"\.", i[0])):
        start, stop = i[0].split("..")
        item.extend([start, stop, i[1]])
        flats.append([int(j) for j in item])
    else:
        start, stop = i[1].split("..")
        item.extend([i[0], start, stop])
        verticals.append([int(j) for j in item])

flats.sort(key=lambda x: x[2])
verticals.sort()

# draw board
min_y = min(min([i[2] for i in flats]), min(i[1] for i in verticals))
max_y = max(max([i[2] for i in flats]), max(i[2] for i in verticals)) + 1
min_x = min(min([i[0] for i in flats]), min([i[0] for i in verticals])) - 1
max_x = max(max([i[1] for i in flats]), max([i[0] for i in verticals])) + 1

board = [["."]*(max_x-min_x+1) for i in range(max_y+1)]


# fill board
for flat in flats:
    for i in range(flat[0], flat[1]+1):
        board[flat[2]][i-min_x] = "#"

for vert in verticals:
    for i in range(vert[1], vert[2]+1):
        board[i][vert[0]-min_x] = "#"

board[0][500-min_x] = "+"

# fill
streams = deque()
visited = set()
streams.append((1, 500))
visited.add((1, 500))

while streams:
    top = streams.popleft()
    board[top[0]][top[1]-min_x] = "|"

    if top[0]+1 != len(board):
        if board[top[0]+1][top[1]-min_x] != "#" and board[top[0]+1][top[1]-min_x] == ".":
            # has to continue flowing down
            if (top[0]+1, top[1]) not in visited:
                streams.append((top[0]+1, top[1]))
                visited.add((top[0]+1, top[1]))
        elif board[top[0]+1][top[1]-min_x] == "|":
            # reached a previously visited cup
            continue
        else:
            # we have reached a flat, fill
            # fill upwards
            current_height = top[0]
            while True:
                valid_range = True
                m_left = top[1]-min_x
                m_right = top[1]-min_x

                while m_left > -1 and (board[current_height][m_left-1] == "." or board[current_height][m_left-1] == "|"):
                    m_left -= 1
                    if board[current_height+1][m_left] == "." or board[current_height+1][m_left] == "|":
                        valid_range = False
                        break

                while m_right < len(board[0]) and (board[current_height][m_right+1] == "." or board[current_height][m_right+1] == "|"):
                    m_right += 1
                    if board[current_height+1][m_right] == "." or board[current_height+1][m_right] == "|":
                        valid_range = False
                        break

                if not valid_range:
                    for i in range(m_left, m_right+1):
                        if (current_height, i+min_x) not in visited:
                            streams.append((current_height, i+min_x))
                            visited.add((current_height, i+min_x))

                    break
                else:
                    for i in range(m_left, m_right+1):
                        board[current_height][i] = "~"
                current_height -= 1

flow_count = 0
water_count = 0

for i in range(min_y, max_y):
    for j in range(len(board[0])):
        cell = board[i][j]
        if cell == "|":
            flow_count += 1
        elif cell == "~":
            water_count += 1

# print board
for level in board:
    print("".join(level))

print(min_x, max_x, min_y, max_y)
print("Total water: ", flow_count+water_count)
print("Still water: ", water_count)
print("Moving water: ", flow_count)
