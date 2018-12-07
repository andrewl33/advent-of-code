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
  def find_root(d, s):

    if len(d) == 0:
      return ''

    roots = []

    for k_1 in d.keys():
      if k_1 in s:
        continue

      is_root = True

      for v in d.values():
        if k_1 in v:
          is_root = False
          break

      if is_root:
        roots.append(k_1)

    roots.sort()

    if roots:
      last = ''
      if len(d) == 1:
        last = d[roots[0]][0]
      s.add(roots[0])
      return roots[0] + last
    return ''


  # transform values to ordered list
  for k, v in d.items():
    d[k] = sorted(list(v), reverse=True)

  # fill in initial work
  worked = set()
  root = ''
  workers = []
  counter = 0
  last = ''

  for _ in range(5):
    root = find_root(d, worked)
    if root != '':
      workers.append((root, ord(root)+1-ord("A")+60))

  # loop til the finish
  while workers:
    counter+=1
    workers = [(r, i-1) for r, i in workers]
    for r, i in workers[:]:
      if i == 0:
        if r in d:
          del d[r]
        workers.remove((r, i))

    while len(workers) < 5:
      root = find_root(d, worked)
      if root == '':
        break
      if len(root) == 2:
        root, last = list(root)
      workers.append((root, ord(root)+1-ord("A")+60))

  # last dep
  counter+=ord(last)+1-ord("A")+60
  return counter


print(solution())