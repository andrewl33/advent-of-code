def solution():

  in_str = ""

  # read file
  with open("input.txt") as file:
    in_str = file.read()

  # make into array
  in_str = list(in_str)

  # reduce
  i = len(in_str) - 1
  while i > 0:
    if in_str[i] != in_str[i-1] and in_str[i].lower() == in_str[i-1].lower():
      del in_str[i]
      del in_str[i-1]
      if i > len(in_str) - 1:
        i = len(in_str) - 1
      else:
        i = max(i - 1, 1)
    else:
      i = i - 1



  return len(in_str)
print(solution())