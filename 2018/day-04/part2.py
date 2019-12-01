import datetime

def solution():
  
  in_arr = []
  
  with open("input.txt") as file:
    for line in file:
      
      # arr to append to arr
      item = []

      # handle date
      d = line[6:11]
      t = line[12:17]
      t = list(map(lambda x: int(x), t.split(":")))
      item.append(d)
      item.append(t[1])

      # handle user
      user_str = line[19:]
      user_str = user_str.split(" ")
      if len(user_str) < 4:
        item.append(user_str[0])
      else:
        item.append(int(user_str[1].replace("#", "")))

      # append item to arr
      in_arr.append(item)

  # sort by date
  in_arr = sorted(in_arr, key=lambda x: (x[0], x[1]))

  # get time asleep
  cur_guard = in_arr[0][2]
  sleep = None
  cur_sleeping = cur_guard

  d = dict()
  d[cur_guard] = dict([(i, 0) for i in range(60)])

  for i in range(1, len(in_arr)):
    if in_arr[i][2] == "falls":
      cur_sleeping = cur_guard
      sleep = in_arr[i][1]
    elif in_arr[i][2] == "wakes":
      for j in range(sleep, in_arr[i][1]):
        d[cur_sleeping][j] = d[cur_sleeping][j] + 1
    else:
      cur_guard = in_arr[i][2]
      if not cur_guard in d:
        d[cur_guard] = dict([(k,0) for k in range(60)])
  
  # get highest minutes
  max_dict = []

  for k, v in d.items():
    max_minute = 0
    max_amount = v[0]
    sum_mins = 0 
    
    for a,b in v.items():
      sum_mins+=b
      if max_amount < b:
        max_minute = a
        max_amount = b
    
    max_dict.append((k, sum_mins, max_minute, max_amount))

  max_dict.sort(key=lambda x: x[3], reverse=True)
  # for item in in_arr:
  return max_dict[0][0] * max_dict[0][2]


print(solution())