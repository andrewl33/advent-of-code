'''

a node wraps its children

c#, m#, (recursively go down), real meta data

'''

# input
input_arr = []
with open("input.txt") as file:
  input_arr = file.read().split(" ")

# process input

input_arr = [int(i) for i in input_arr]

meta = []

def rec_aux(i):
  c, m = input_arr[i:i+2]
  i+=2
  for _ in range(c):
    i = rec_aux(i)
  meta.append(sum(input_arr[i:i+m]))
  return i+m

rec_aux(0)

print(sum(meta))