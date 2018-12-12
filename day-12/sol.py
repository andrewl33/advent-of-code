

in_state = "##.#..########..##..#..##.....##..###.####.###.##.###...###.##..#.##...#.#.#...###..###.###.#.#"
test_state = "#..#.#..##......###...###"



P = "input.txt"
TEST_P = "test.txt"
GEN = 500
# GEN = 20

with open(P) as file:
  patterns = {k:v for (k,v) in [(line[:5], line[9]) for line in file]}

  state = in_state
  in_state_len = len(state)

  state_end = 0

  change = [0]*GEN

  for i in range(GEN):
    state = "".join([".....", state, "....."])
    new_state = ""
    for j in range(2, len(state) - 2):
      pat = state[j-2:j+3]
      new_state = "".join([new_state, patterns[pat]])

    # slice off tail
    state_end-=3
    cur_idx = 0
    cur_neg_idx = len(new_state)
    while new_state[cur_idx] != "#":
      cur_idx+=1
    
    while new_state[cur_neg_idx-1] != "#":
      cur_neg_idx-=1

    state_end+=cur_idx
    new_state = new_state[cur_idx:cur_neg_idx]

    state = new_state

    # check for patterns
    change[i] = sum([x + state_end for x in range(len(state)) if state[x] == "#"])
    print(change[i] - change[i-1])

    if change[i]- change[i-1] == 45:
      print(i, sum([x + state_end for x in range(len(state)) if state[x] == "#"]))



  # count sum again
  print(state)
  print([i + state_end for i in range(len(state)) if state[i] == "#"]) 
  print(sum([i + state_end for i in range(len(state)) if state[i] == "#"]))


# 50000000000 answer
print(22620 + 45 * (50000000000 - 500))