'''
Create a checksum for boxes
The checksum is produced by # of strings with at least exactly two of one letter
multipled by the number of strings with at least exactly three of one letter
A string can contain more than one repeat, and a string can count for both 2 and 3 repeats
'''

def solution():
  file_name = "input.txt"
  two_count = 0
  three_count = 0
  with open(file_name) as file:
    for line in file:
      # before
      d = dict()
      found_two = False
      found_three = False

      # fill dictionary
      for ch in list(line):
        
        if ch in d:
          d[ch] = d[ch] + 1
        else:
          d[ch] = 1

      # find values with 2 or 3
      for item in d.items():
        if item[1] == 2 and not found_two:
          two_count+=1
          found_two = True
        if item[1] == 3 and not found_three:
          three_count+=1
          found_three = True
        if found_two and found_three:
          break
  
  return two_count * three_count

print(solution())