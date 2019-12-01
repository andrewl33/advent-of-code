'''
BFS solution, O((w*h)^2)
w and h can be large
'''

from collections import deque

def solution(flex):

    # read file
    coords = []
    with open('input.txt') as file:
        for line in file:
            a, b = line.split(',')
            coords.append((int(a), int(b)))

    x_low = max(min([x for x, y in coords]) - flex, 0)
    x_high = max([x for x, y in coords]) + flex
    y_low = max(min([y for x, y in coords]) - flex, 0)
    y_high = max([y for x, y in coords]) + flex

    max_depth = (x_high-x_low) * (y_high-y_low)

    # board
    d = dict([((x, y), (max_depth, (-1, -1), False)) for x in range(x_low, x_high+1)
              for y in range(y_low, y_high+1)])

    # coord set for quick lookup
    coords_s = set(coords)

    # run bfs on each cell
    for k, v in d.items():

        # skip if real point
        if (k) in coords_s:
            d[k] = ((max_depth,(-1, -1), True))
            continue

        min_depth = max_depth
        visited = set()
        dq = deque()
        found = 0
        visited.add((k[0], k[1]))
        dq.append((k[0], k[1], 0))

        while dq and found < 2:
            # make sure valid locations, and less than min_depth
            front = dq.popleft()
            # have to pass through every one, to see if there are collisions
            if front[2]+1 <= min_depth:
                if front[0] - 1 >= x_low and not (front[0]-1, front[1]) in visited:
                    visited.add((front[0]-1, front[1]))
                    if (front[0]-1, front[1]) in coords_s:
                        found+=1
                        min_depth = min(min_depth, front[2]+1)
                        d[k] = (min_depth, (front[0]-1, front[1]), False)
                    else:
                        dq.append((front[0]-1, front[1], front[2]+1))
                if front[0] + 1 <= x_high and not (front[0]+1, front[1]) in visited:
                    visited.add((front[0]+1, front[1]))
                    if (front[0]+1, front[1]) in coords_s:
                        found+=1
                        min_depth = min(min_depth, front[2]+1)
                        d[k] = (min_depth, (front[0]+1, front[1]), False)
                    else:
                        dq.append((front[0]+1, front[1], front[2]+1))
                if front[1] - 1 >= y_low and not (front[0], front[1]-1) in visited:
                    visited.add((front[0], front[1]-1))
                    if (front[0], front[1]-1) in coords_s:
                        found+=1
                        min_depth = min(min_depth, front[2]+1)
                        d[k] = (min_depth, (front[0], front[1]-1), False)
                    else:
                        dq.append((front[0], front[1]-1, front[2]+1))
                if front[1] + 1 <= y_high and not (front[0], front[1]+1) in visited:
                    visited.add((front[0], front[1]+1))
                    if (front[0], front[1]+1) in coords_s:
                        found+=1
                        min_depth = min(min_depth, front[2]+1)
                        d[k] = (min_depth, (front[0], front[1]+1), False)
                    else:
                        dq.append((front[0], front[1]+1, front[2]+1))
        
        if found > 1:
            d[k] = ((max_depth,(-1, -1), True))
            

    # find largest area
    count_area = dict([(i, 0) for i in coords])

    for k,v in d.items():
        if not v[2]:
            count_area[v[1]] = count_area[v[1]] + 1
    
    # remove edge areas

    filtered_dict = count_area.copy()

    for k in count_area.keys():
        for d_k, v in d.items():
            if d_k[0] == x_low or d_k[0] == x_high or d_k[1] == y_low or d_k[1] == y_high:
                if k == v[1]:
                    del filtered_dict[k]
                    break

    return max(max(filtered_dict.values())+1, 0)

print(solution(2))
print(solution(50))