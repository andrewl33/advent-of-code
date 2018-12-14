'''
two elves
creates digits of the sum of the current recipe

'''

puzzle_input = 286051


elf1 = 0
elf2 = 1

recipes = [3,7]
bot = puzzle_input
top = 10

while len(recipes) < bot+top:
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


print("".join([str(i) for i in recipes][bot:bot+top]))
