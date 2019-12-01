import re

input_arr = []

with open("input.txt") as file:
  input_arr = [[int(i) for i in re.findall(r'-?\d+', line)] for line in file]

least_arr = []

bot = 10607
top = 10652

# find the smallest area
for i in range(bot, top):

  min_x = min([i * vx + x for x, _, vx, _ in input_arr])
  max_x = max([i * vx + x for x, _, vx, _ in input_arr])
  min_y = min([i * vy + y for _, y, _ ,vy in input_arr])
  max_y = max([i * vy + y for _, y, _ ,vy in input_arr])
  
  print(i, (max_x - min_x) * (max_y - min_y), min_x, max_x, min_y, max_y)

# draw to console
test = 10630
draw = [[' '] * 150 for _ in range(200)]

for x, y, vx, vy in input_arr:
  draw[x + vx * test][y + vy * test - 100] = '#'

for j in range(len(draw)):
  print(''.join(draw[j]))
