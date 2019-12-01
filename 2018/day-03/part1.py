'''
l, w >= 1000
claim:
  id
  inches btw left edge and left edge
  inches btw top edge and top edge
  w
  h
  ex: #123 @ 3,2: 5x4

  find overlapping claims
'''

def solution():
  d = dict()

  with open("input.txt") as file:
    for line in file:
      in_arr = line.split(" ")
      start = in_arr[2].split(",")
      start[1] = start[1].replace(":", "")
      in_arr[3]= in_arr[3].replace("\n", "")
      dim = in_arr[3].split("x")

      for i in range(int(start[0]), int(start[0]) + int(dim[0])):
        for j in range(int(start[1]), int(start[1]) + int(dim[1])):
          if (i, j) in d:
            d[(i,j)] = d[(i,j)] + 1
          else:
            d[(i,j)] = 1
    
  return len([k for (k,v) in d.items() if v > 1])

print(solution())