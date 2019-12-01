'''

a node wraps its children

c#, m#, (recursively go down), real meta data

no nodes = sum of metadata

has nodes = metadata entries become node values

'''

# input
input_arr = []
with open("input.txt") as file:
  input_arr = file.read().split(" ")

# process input

input_arr = [int(i) for i in input_arr]

def rec_aux(i):
  c, m = input_arr[i:i+2]
  i+=2
  meta_dict = dict()
  for x in range(c):
    i, total = rec_aux(i)
    meta_dict[x+1] = total
  if c > 0:
    return (i+m, sum([meta_dict[x] for x in input_arr[i:i+m] if x in meta_dict]))
  else:
    return (i+m ,sum(input_arr[i:i+m]))


  return i+m

print(rec_aux(0)[1])

