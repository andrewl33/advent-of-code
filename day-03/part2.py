# find dict items with only 1 value
def solution():
  
  d = dict()

  id_arr = []

  with open("input.txt") as file:
    for line in file:
      in_arr = line.split(" ")
      start = in_arr[2].split(",")
      start[1] = start[1].replace(":", "")
      in_arr[3]= in_arr[3].replace("\n", "")
      dim = in_arr[3].split("x")

      id_arr.append((in_arr[0], int(start[0]), int(start[0]) + int(dim[0]), int(start[1]), int(start[1]) + int(dim[1])))

      for i in range(int(start[0]), int(start[0]) + int(dim[0])):
        for j in range(int(start[1]), int(start[1]) + int(dim[1])):
          if (i, j) in d:
            d[(i,j)] = d[(i,j)] + 1
          else:
            d[(i,j)] = 1

    for name, start_x, end_x, start_y, end_y in id_arr:
      count = 0
      for i in range(start_x, end_x):
        for j in range(start_y, end_y):
          if d[(i,j)] == 1:
            count+=1

      if (end_x - start_x) * (end_y - start_y) == count:
        return name

    return None


print(solution())