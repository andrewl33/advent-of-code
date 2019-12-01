puzzle_input = 286051

elf1 = 0
elf2 = 1

recipes = [3,7]
bot = puzzle_input
top = 10

while True:
  # add together
  new_recipes = recipes[elf1] + recipes[elf2]
  # append
  if new_recipes >= 10:
    recipes.append(1)
    recipes.append(new_recipes % 10)
  else:
    recipes.append(new_recipes)
  
  # move elf
  elf1 = (recipes[elf1] + 1 + elf1) % len(recipes)
  elf2 = (recipes[elf2] + 1 + elf2) % len(recipes) 

  if elf1 == elf2:
    elf2 = (elf2 + 1) % len(recipes)

  # not necessary

  # pretty print
  # out = [" " + str(i)  +" " for i in recipes]
  # out[elf1] = "(" + str(recipes[elf1]) + ")"
  # out[elf2] = "[" + str(recipes[elf2]) + "]"
  # print(" ".join(out))
  # print( int("".join([str(i) for i in recipes[len(recipes) - 6:]])))
  print(len(recipes))
  if len(recipes) > 6 and (int("".join([str(i) for i in recipes[len(recipes)-6:]])) == puzzle_input or int("".join([str(i) for i in recipes[len(recipes)-7:len(recipes)-1]])) == puzzle_input):
    print(recipes[len(recipes) - 7:])
    print(len(recipes))
    break
  
print(len(recipes)-6)
print(len(recipes)-7)


# 20195121
# [2, 8, 6, 0, 5, 1, 2]
# 20195121
# 20195115
# 20195114