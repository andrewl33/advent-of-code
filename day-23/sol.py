'''
using manhattan distance, find things in range <= signal radius

going to make a directed graph, where a dict of positions and sets  shows what it can reach
'''

# part 1, find nanobots that are in range of the signal

# get input

# key: (x,y,z,r) = set of in range
in_range = {}

with open('input.txt') as file:
    for line in file:
        l, r = line.split()
        l = [int(i) for i in l[5:len(l)-2].split(',')]
        r = int(r[2:])
        in_range[(l[0], l[1], l[2], r)] = set()


def md(a, b):
    return sum([abs(a[0]-b[0]), abs(a[1]-b[1]), abs(a[2]-b[2])])


for k in in_range.keys():
    for a in in_range.keys():
        if k == a:
            continue
        elif md(k, a) <= k[3]:
            in_range[k].add(a)


# part 1
print(max(in_range, key=lambda x: x[3]))
print(len(in_range[(70283314, 68684712, -30543765, 99305649)]))

# part 2
# manhattan distance from 0,0,0 to the point in range of most bots
'''
build a 3d graph with each item having a set of valid; return length of largest
takes 3 * n * 100 mil ^ 3 time

check around each point, starting from the largest one
too hard

gonna try the z3 library (heavily relying on reddit answers for this one)
full credit to: https://github.com/msullivan/advent-of-code/blob/master/2018/23b.py
'''

from z3 import *


def z3_abs(x):
    return If(x >= 0, x, -x)


def z3_dist(x, y):
    return z3_abs(x[0] - y[0]) + z3_abs(x[1] - y[1]) + z3_abs(x[2] - y[2])


# fit my in_range to msullivan's in_range
in_range = [(x[3], (x[0], x[1], x[2]))
            for x in in_range.keys()]

# create variables
x = Int('x')
y = Int('y')
z = Int('z')

# values
orig = (x, y, z)

# expression to optimize
cost_expr = x * 0
for r, pos in in_range:
    cost_expr += If(z3_dist(orig, pos) <= r, 1, 0)

# op object
opt = Optimize()

# adds functions to optimize
opt.maximize(cost_expr)
opt.minimize(z3_dist((0, 0, 0), (x, y, z)))

# check against sat
opt.check()

# returns value from last check
model = opt.model()

print(model)
print(md((0, 0, 0), (model[x].as_long(),
                     model[y].as_long(), model[z].as_long())))
