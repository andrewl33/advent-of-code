'''
. open ground
| trees
# lumberyard

open -> trees if 3 ore more adj acres contains trees
tree -> lumber 3 or more adj acres were lumberyards
lumberyard -> open not adj to at least one lumber and at least one acre
'''
# inputs
PART_1 = 10
PART_2 = 1000000000

# get input
yard = []
y_len = 0
x_len = 0
with open("input.txt") as file:
    yard = [list(line) for line in file]
    y_len = len(yard)
    x_len = len(yard[0]) - 1
    yard = [item for sublist in yard for item in sublist if item != "\n"]

cur_count = yard.count("|") * yard.count("#")
next_count = yard.count("|") * yard.count("#")
visited = set()
for _ in range(1):

    if next_count - cur_count in visited:
        print(_, cur_count, len(visited))
    else:
        print(_, next_count - cur_count)
        visited.add(next_count - cur_count)
    next_count = cur_count

    next_yard = []
    for i in range(y_len):
        for j in range(x_len):
            adj_list = []
            if i > 0:
                adj_list.append(yard[(i-1)*x_len + j])
                if j > 0:
                    adj_list.append(yard[(i-1)*x_len + j-1])
                if j < x_len-1:
                    adj_list.append(yard[(i-1)*x_len + j+1])
            if i < y_len-1:
                adj_list.append(yard[(i+1)*x_len + j])
                if j > 0:
                    adj_list.append(yard[(i+1)*x_len + j-1])
                if j < x_len-1:
                    adj_list.append(yard[(i+1)*x_len + j+1])
            if j < x_len-1:
                adj_list.append(yard[i*x_len + j+1])
            if j > 0:
                adj_list.append(yard[i*x_len + j-1])

            if yard[(i*x_len + j)] == ".":
                if adj_list.count("|") >= 3:
                    next_yard.append("|")
                else:
                    next_yard.append(".")
            elif yard[(i*x_len+j)] == "|":
                if adj_list.count("#") >= 3:
                    next_yard.append("#")
                else:
                    next_yard.append("|")
            elif yard[(i*x_len+j)] == "#":
                if adj_list.count("#") > 0 and adj_list.count("|") > 0:
                    next_yard.append("#")
                else:
                    next_yard.append(".")
    yard = next_yard.copy()
    cur_count = yard.count("|") * yard.count("#")

# output
print("Resource value after (%d): " %
      PART_2, yard.count("|") * yard.count("#"))

'''
2542 201000 530
2543 206040 530
2544 206180 530
2545 212711 530
2546 214368 530
2547 218680 530
2548 217448 530
2549 220785 530
2550 219708 530
2551 216804 530
2552 214271 530
2553 211552 530
2554 205771 530
2555 204863 530
2556 199386 530
2557 196860 530
2558 192718 530
2559 193438 530
2560 189090 530
2561 190568 530
2562 190080 530
2563 191649 530
2564 190314 530
2565 193966 530
2566 193781 530
2567 196876 530
2568 197276 530 #
2569 202722 530
2570 201000 530

loops at 28
1000000000 - (28*x) = somewhere in 2570 to 2542
x = (1000000000 - (somewhere in 2570 to 2542) / 28)
'''

for i in range(28):
    print(i+2542, (PART_2 - (i+2542)) / 28)
