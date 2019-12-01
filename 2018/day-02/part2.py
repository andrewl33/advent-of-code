'''
Differ by one in the same position
Return all the other characters that are the same other than
the differing character

There are only two box IDs with only one differing letter
id length has to be greater than two
id length has to be all equal
'''

def solution():
  f_name = "input.txt"

  id_arr = []

  # add all char lists to id_arr
  with open(f_name) as file:
    for line in file:
      id_arr.append(list(line))
      id_arr[-1].pop()
    
  # check for diffs O(n^2 * m), where n is lines, m is id length
  for i in range(len(id_arr)):
    for j in range(i, len(id_arr)):
      diff = 0
      diff_idx = 0
      char_idx = 0
      while char_idx < len(id_arr[i]):
        if id_arr[i][char_idx] != id_arr[j][char_idx]:
          diff+=1
          diff_idx = char_idx
        if diff > 1:
          break
        char_idx+=1
      
      if diff == 1:
        id_arr[i].pop(diff_idx)
        return id_arr[i]

print(''.join(solution()))
        