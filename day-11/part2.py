'''
Same thing, any size
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

maxTotal = grid[0][0]
maxCoord = (0,0)
maxSize = 1

# O(n^4), yikes!!
for i in range(300-3):
  for j in range(300-3):
    localMax = 0
    print(i,j)
    for k in range(min(297-i, 297-j)):

      for l in range(i, i+k):
        localMax+=grid[l][j+k]
      for m in range(j, j+k):
        localMax+=grid[i+k][m]
      localMax += grid[i+k][j+k]

      if localMax > maxTotal:
        maxTotal = localMax
        maxCoord = (i+1,j+1)
        maxSize = k+1

print(maxCoord, maxSize)