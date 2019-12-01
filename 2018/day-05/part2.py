def solution():

  in_str = ""

  # read file
  with open("input.txt") as file:
    in_str = file.read()

  # make into array
  in_str = list(in_str)

  # find unique letters
  unique_letters = list(set([x.lower() for x in in_str]))

  # define min
  min_size = len(in_str)


  for letter in unique_letters:
    copy_in_str = [x for x in in_str if x.lower() != letter]

    # reduce
    i = len(copy_in_str) - 1
    while i > 0:
      if copy_in_str[i] != copy_in_str[i-1] and copy_in_str[i].lower() == copy_in_str[i-1].lower():
        del copy_in_str[i]
        del copy_in_str[i-1]
        if i > len(copy_in_str) - 1:
          i = len(copy_in_str) - 1
        else:
          i = max(i - 1, 1)
      else:
        i = i - 1
    
    min_size = min(min_size, len(copy_in_str))


  return min_size


print(solution())