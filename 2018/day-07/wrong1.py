'''
topological sort, with a sort alphabetically

shows the order by least dependent
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
  roots = []

  for k_1 in d.keys():
    is_root = True
    for v in d.values():
      if k_1 in v:
        is_root = False
        break
    
    if is_root:
      roots.append(k_1)


  # transform values to ordered list
  for k, v in d.items():
    d[k] = sorted(list(v), reverse=True)


  # run level order search
  ordered_arr = []
  visited = set(roots)
  cur_level = set(roots)
  next_level = set()

  for i in cur_level:
    for j in d[i]:
      next_level.add(j)


  # creates sets for each tier
  while len(next_level) > 0:
    ordered_arr.append(cur_level)
    cur_level = next_level.copy()
    next_level.clear()

    for i in cur_level:
      # bubble to cur_level
      if i in visited:
        for j in ordered_arr:
          if i in j:
            j.remove(i)
      
      # add to visited
      visited.add(i)

      # add to next level
      if i in d:
        for v in d[i]:
          next_level.add(v)
  
  # add last tier
  for i in cur_level:
    # bubble to cur_level/last level
    if i in visited:
      for j in ordered_arr:
        if i in j:
          j.remove(i)

  ordered_arr.append(cur_level)

  # create printable format
  ordered_arr = [item for sublist in [sorted(list(i)) for i in ordered_arr] for item in sublist]

  return "".join(ordered_arr)


print(solution())