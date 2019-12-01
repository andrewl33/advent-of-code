'''
Finds least dependent, alphabetically
O(n^3)
'''

def solution():
  
  # get input O(n)
  pairs = []

  with open("input.txt") as file:
    for line in file:
      split = line.split()
      dep = split[1]
      ind = split[7]
      pairs.append((dep, ind))

  # order for better reading
  pairs.sort()

  # put in "nodes" O(n)
  d = dict()

  for p in pairs:
    if not p[0] in d:
      d[p[0]] = set(p[1])
    else:
      d[p[0]].add(p[1])

  # find degree 0 O(n^2)
  def find_roots(d):
    if len(d) == 0:
      return []

    roots = []

    for k_1 in d.keys():
      is_root = True
      for v in d.values():
        if k_1 in v:
          is_root = False
          break
      
      if is_root:
        roots.append(k_1)
    return roots



  # transform values to ordered list
  for k, v in d.items():
    d[k] = sorted(list(v), reverse=True)

  # least dependent search O(n)
  roots = find_roots(d)
  out_arr = []
  while roots:

    out_arr.append(roots[0])
    
    # remove from dict
    if (len(d) == 1):
      out_arr.append(d[out_arr[-1]][0])
    del d[roots[0]]

    # find the head
    roots = find_roots(d)

  
  return ("").join(out_arr)

print(solution())