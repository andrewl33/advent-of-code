from collections import deque

def problem(hitpoints):
    with open("input.txt") as file:
        cave = [list(line.rstrip("\n")) for line in file]
        hp = {}

        # fill dict
        for i in range(len(cave)):
            for j in range(len(cave[i])):
                if cave[i][j] == "E" or cave[i][j] == "G":
                    hp[(i, j)] = [cave[i][j], 200, False]

        # run game
        game_count = 1
        # for _ in range(10):
        while True:

            # cleanup before
            for k, v in hp.items():
                hp[k] = [v[0], v[1], False]

            for i in range(len(cave)):
                for j in range(len(cave[i])):

                    if (i, j) in hp and not hp[(i, j)][2]:
                        hp[(i,j)][2] = True
                        # find opposite
                        opposite = ''
                        if hp[(i, j)][0] == "E":
                            opposite = "G"
                        else:
                            opposite = "E"

                        def attack(i, j):
                            opposite_char = None
                            # handle attack
                            if cave[i-1][j] == opposite:
                                opposite_char = (i-1, j)
                            if cave[i][j-1] == opposite:
                                if opposite_char:
                                    if hp[(opposite_char[0], opposite_char[1])][1] > hp[(i, j-1)][1]:
                                        opposite_char = (i, j-1)
                                else:
                                    opposite_char = (i, j-1)
                            if cave[i][j+1] == opposite:
                                if opposite_char:
                                    if hp[(opposite_char[0], opposite_char[1])][1] > hp[(i, j+1)][1]:
                                        opposite_char = (i, j+1)
                                else:
                                    opposite_char = (i, j+1)
                            if cave[i+1][j] == opposite:
                                if opposite_char:
                                    if hp[(opposite_char[0], opposite_char[1])][1] > hp[(i+1, j)][1]:
                                        opposite_char = (i+1, j)
                                else:
                                    opposite_char = (i+1, j)

                            # there was one to attack
                            if opposite_char is not None:
                                atk = 3
                                if opposite == "G":
                                    atk = hitpoints
                                if hp[(opposite_char[0], opposite_char[1])][1] - atk < 1:
                                    cave[opposite_char[0]][opposite_char[1]] = "."
                                    del hp[(opposite_char[0], opposite_char[1])]
                                    
                                else:
                                    hp[(opposite_char[0], opposite_char[1])][1] -= atk
                                return True
                            return False
                        # nothing to attack; search for something close
                        if not attack(i,j):
                            visited = dict()
                            visited_flat = set()
                            dq = deque()
                            nearest = []
                            dq.append((i, j))
                            depth = 0

                            while len(dq) > 0:
                                depth += 1
                                if nearest and min([d[2] for d in nearest]) < depth:
                                    break
                                x, y = dq.popleft()
                                visited[(x, y)] = set()
                                # check each in reading order

                                if cave[x-1][y] != "#":
                                    if cave[x-1][y] == "." and not (x-1, y) in visited and not (x-1, y) in visited_flat:
                                        dq.append((x-1, y))
                                        visited[(x, y)].add((x-1, y))
                                        visited_flat.add((x-1, y))
                                    elif cave[x-1][y] == opposite:
                                        nearest.append([x-1, y, depth])
                                        visited[(x, y)].add((x-1, y))

                                if cave[x][y-1] != "#":
                                    if cave[x][y-1] == "." and not (x, y-1) in visited and not (x, y-1) in visited_flat:
                                        dq.append((x, y-1))
                                        visited[(x, y)].add((x, y-1))
                                        visited_flat.add((x, y-1))
                                    elif cave[x][y-1] == opposite:
                                        nearest.append([x, y-1, depth])
                                        visited[(x, y)].add((x, y-1))

                                if cave[x][y+1] != "#":
                                    if cave[x][y+1] == "." and not (x, y+1) in visited and not (x, y+1) in visited_flat:
                                        dq.append((x, y+1))
                                        visited[(x, y)].add((x, y+1))
                                        visited_flat.add((x, y+1))
                                    elif cave[x][y+1] == opposite:
                                        nearest.append([x, y+1, depth])
                                        visited[(x, y)].add((x, y+1))

                                if cave[x+1][y] != "#":
                                    if cave[x+1][y] == "." and not (x+1, y) in visited and not (x+1, y) in visited_flat:
                                        dq.append((x+1, y))
                                        visited[(x, y)].add((x+1, y))
                                        visited_flat.add((x+1, y))
                                    elif cave[x+1][y] == opposite:
                                        nearest.append([x+1, y, depth])
                                        visited[(x, y)].add((x+1, y))

                            def reading_order(x):
                                return (x[1], x[0])

                            # get closest if it exists
                            if nearest:
                                minimum = min([i[2] for i in nearest])
                                nearest = [i for i in nearest if i[2] == minimum]
                                nearest.sort(key=reading_order)
                                cur = (nearest[0][0], nearest[0][1])
                                # loop back
                                while cur:
                                    if cur in visited[(i, j)]:
                                        cave[cur[0]][cur[1]] = cave[i][j]
                                        cave[i][j] = "."
                                        hp[(cur[0], cur[1])] = hp[(i, j)].copy()
                                        hp[(cur[0], cur[1])][2] = True
                                        del hp[(i, j)]
                                        attack(cur[0], cur[1])
                                        break
                                    else:
                                        for k, v in visited.items():
                                            if cur in v:
                                                cur = k
                                                break
            # check if empty
            g_count = 0
            e_count = 0

            for v in hp.values():
                if v[0] == "G":
                    g_count += 1
                else:
                    e_count += 1
            if e_count != 10:
                return False
            elif g_count == 0:
                print(sum([i[1] for i in hp.values()]) * (game_count-1))
                print(sum([i[1] for i in hp.values()]) * (game_count))
                return True
            else:
                game_count += 1

count = 4
while not problem(count):
    print("try ", count)
    count+=1