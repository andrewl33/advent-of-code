with open("input.txt") as file:


  cart_set = set(["<", ">", "^", "v"]) 

  order = ["l", "s", "r"]

  board = []

  for line in file:
    board.append(list(line.rstrip('\n')))
  
  # cart_dict
  cart_dict = dict()

  # find carts
  for i in range(len(board)):
    for j in range(len(board[i])):
      if board[i][j] in cart_set:
        if board[i][j] == "v" or board[i][j] == "^":
          cart_dict[(i,j)] = (0, "|", False)
        else:
          cart_dict[(i,j)] = (0, "-", False)
  print(cart_dict)
  # cart move priority is 0,0 to len, len
  cont = True
  while len(cart_dict) > 1:
    for i in range(len(board)):
      for j in range(len(board[i])):
        if (i, j) in cart_dict:
          if cart_dict[(i,j)][2]: # touched
            continue
          cell = board[i][j]
          
          # route
          # <
          if cell == "<":
            
            # crash
            if (i, j-1) in cart_dict:
              board[i][j] = cart_dict[(i,j)][1]
              board[i][j-1] = cart_dict[(i, j-1)][1]
              del cart_dict[(i,j)]
              del cart_dict[(i, j-1)]
            else:
              if board[i][j-1] == "/":
                board[i][j-1] = "v"
                cart_dict[(i, j-1)] = (cart_dict[(i,j)][0], "/", True)
              elif board[i][j-1] == "\\":
                board[i][j-1] = "^"
                cart_dict[(i, j-1)] = (cart_dict[(i,j)][0], "\\", True)
              elif board[i][j-1] == "+":
                direction = order[cart_dict[(i, j)][0]]
                if direction == "l":
                  board[i][j-1] = "v"
                elif direction == "s":
                  board[i][j-1] = "<"
                else:
                  board[i][j-1] = "^"

                cart_dict[(i, j-1)] = (cart_dict[(i,j)][0] + 1, "+", True)

              else:
                board[i][j-1] = "<"
                cart_dict[(i, j-1)] = (cart_dict[(i,j)][0], "-", True)
              
              # cleanup
              board[i][j] = cart_dict[(i,j)][1]

          # >
          elif cell == ">":
            
            #crashed
            if (i, j+1) in cart_dict:
              board[i][j] = cart_dict[(i,j)][1]
              board[i][j+1] = cart_dict[(i, j+1)][1]
              del cart_dict[(i,j)]
              del cart_dict[(i, j+1)]          
            else:
              if board[i][j+1] == "\\":
                board[i][j+1] = "v"
                cart_dict[(i, j+1)] = (cart_dict[(i,j)][0], "\\", True)
              elif board[i][j+1] == "/":
                board[i][j+1] = "^"
                cart_dict[(i, j+1)] = (cart_dict[(i,j)][0], "/", True)
              elif board[i][j+1] == "+":

                direction = order[cart_dict[(i, j)][0]]

                if direction == "l":
                  board[i][j+1] = "^"
                elif direction == "s":
                  board[i][j+1] = ">"
                else:
                  board[i][j+1] = "v"
                
                cart_dict[(i, j+1)] = (cart_dict[(i,j)][0] + 1, "+", True)

              else:
                board[i][j+1] = ">"
                cart_dict[(i, j+1)] = (cart_dict[(i,j)][0], "-", True)
              
              # cleanup
              board[i][j] = cart_dict[(i,j)][1]

          # ^
          elif cell == "v":
            
            #crashed
            if (i+1, j) in cart_dict:
              board[i][j] = cart_dict[(i,j)][1]
              board[i+1][j] = cart_dict[(i+1, j)][1]
              del cart_dict[(i,j)]
              del cart_dict[(i+1, j)]
            else:
              if board[i+1][j] == "\\":
                board[i+1][j] = ">"
                cart_dict[(i+1, j)] = (cart_dict[(i,j)][0], "\\", True)
              elif board[i+1][j] == "/":
                board[i+1][j] = "<"
                cart_dict[(i+1, j)] = (cart_dict[(i,j)][0], "/", True)
              elif board[i+1][j] == "+":

                direction = order[cart_dict[(i,j)][0]]

                if direction == "l":
                  board[i+1][j] = ">"
                elif direction == "s":
                  board[i+1][j] = "v"
                else:
                  board[i+1][j] = "<"

                cart_dict[(i+1, j)] = (cart_dict[(i,j)][0] + 1, "+", True)
              else:
                board[i+1][j] = "v"
                cart_dict[(i+1, j)] = (cart_dict[(i,j)][0], "|", True)
              
              # cleanup
              board[i][j] = cart_dict[(i,j)][1]          
            

          elif cell == "^":

            if (i-1, j) in cart_dict:
              board[i][j] = cart_dict[(i,j)][1]
              board[i-1][j] = cart_dict[(i-1, j)][1]
              del cart_dict[(i,j)]
              del cart_dict[(i-1, j)]
            else:
              if board[i-1][j] == "\\":
                board[i-1][j] = "<"
                cart_dict[(i-1, j)] = (cart_dict[(i,j)][0], "\\", True)
              elif board[i-1][j] == "/":
                board[i-1][j] = ">"
                cart_dict[(i-1, j)] = (cart_dict[(i,j)][0], "/", True)
              elif board[i-1][j] == "+":

                direction = order[cart_dict[(i, j)][0]]

                if direction == "l":
                  board[i-1][j] = "<"
                elif direction == "s":
                  board[i-1][j] = "^"
                else:
                  board[i-1][j] = ">"

                cart_dict[(i-1, j)] = (cart_dict[(i,j)][0] + 1, "+", True)
              else:
                board[i-1][j] = "^"
                cart_dict[(i-1, j)] = (cart_dict[(i,j)][0], "|", True)
              
              # cleanup
          if (i,j) in cart_dict:
            board[i][j] = cart_dict[(i,j)][1]  
            del cart_dict[(i,j)]

          # exciting countdown!!!
          print(len(cart_dict))
    # mark all dict to false
    cart_dict = {k:(v[0] % 3, v[1], False) for k,v in cart_dict.items()}

  print([(k[1], k[0]) for k in cart_dict.keys()][0])