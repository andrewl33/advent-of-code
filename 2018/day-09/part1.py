PLAYERS = 477
LAST_MARBLE_PTS = 70851

player_pts = [0 for _ in range(PLAYERS+1)]
marble_circle = [0 for _ in range(2)]
current_circle_size = 1
current_person = 1
current_position = 0

# run game
for i in range(1, LAST_MARBLE_PTS+1):

  # first check points
  if i % 23 == 0:
    to_remove = current_position - 7
    if to_remove < 0:
      to_remove += current_circle_size
    player_pts[current_person] += marble_circle[to_remove] + i

    del marble_circle[to_remove]
    marble_circle.append(0)

    current_position = to_remove
    current_circle_size-=1
  
  else:
    # find new position
    current_position = (current_position + 2) % current_circle_size
    marble_circle.insert(current_position, i)
    current_circle_size+=1
    current_person+=1
    if current_person == PLAYERS + 1:
      current_person = 1


print(max(player_pts))