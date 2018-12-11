'''
300x300 grid of fuel cells
top left is 1,1
top right is 300, 1

3x3 square with the largest total power

rackID = x_coord + 10
p_level = rackID * y_coord
p_level+=puzzle input
p_level*=rackID

p_level = Keep hundredth digit or 0
p_level-=5


'''
PUZZLE_INPUT = 8561

grid = [[0] * 300 for _ in range(300)]

for i in range(300):
  for j in range(300):
    rackID = i + 1 + 10
    powerLevel = rackID * (j+1)
    powerLevel += PUZZLE_INPUT
    powerLevel *= rackID

    if powerLevel // 100 > 0:
      powerLevel = (powerLevel // 100) % 10  
    else:
      powerLevel = 0
    
    powerLevel-=5

    grid[i][j] = powerLevel

maxTotal = grid[0][0] + grid[1][0] + grid[2][0] + grid[0][1] + grid[1][1] + grid[2][1] + grid[0][2] + grid[1][2] +grid[2][2]
maxCoord = (0,0)

for i in range(1,300-3):
  for j in range(1,300-3):
    localMax = grid[i][j] + grid[i+1][j] + grid[i+2][j] + grid[i][j+1] + grid[i+1][j+1] + grid[i+2][j+1] + grid[i][j+2] + grid[i+1][j+2] +grid[i+2][j+2]

    if localMax > maxTotal:
      print(maxCoord)
      maxTotal = localMax
      print(maxTotal)
      maxCoord = (i,j)

print(maxCoord[0]+1, maxCoord[1]+1)