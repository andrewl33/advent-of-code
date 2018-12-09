'''
100 times larger lmao
deque.rotate is so much better than my initial part 2
solutions where I shifted pointers around and appended
'''
from collections import deque

PLAYERS = 477
LAST_MARBLE_PTS = 70851 * 100

player_pts = [0 for _ in range(PLAYERS+1)]
marble_circle = deque([0])
current_person = 1

# run game
for i in range(1, LAST_MARBLE_PTS+1):

    # first check points
    if i % 23 == 0:
        marble_circle.rotate(7)
        player_pts[current_person] += marble_circle.pop() + i
        marble_circle.rotate(-1)

    else:
        # find new position
        marble_circle.rotate(-1)
        marble_circle.append(i)
        current_person += 1
        if current_person == PLAYERS + 1:
            current_person = 1


print(max(player_pts))
