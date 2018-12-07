'''
properly use manhattan distance
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

    count = 0

    # Manhattan sum for each
    for x in range(x_low, x_high+1):
        for y in range(y_low, y_high+1):
            temp = [abs(x-i[0])+abs(y-i[1]) for i in coords]
            if sum(temp) < 10000:
                count+=1   

    return count 

print(solution(1))