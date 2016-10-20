import numpy as np
import copy

board = [
  [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
  ],
  [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
  ],
  [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
  ],
  [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
  ]
]


p1_token = 1
p2_token = -1
draw_token = 0


def slice_winner(state_slice):
  slice_size = len(state_slice)
  sums = [sum(row) for row in state_slice]
  sums.extend([sum([row[i] for row in state_slice]) for i in range(slice_size)])

  if (p1_token * slice_size) in sums:
    return p1_token
  elif (p2_token * slice_size) in sums:
    return p2_token

  return 0


def winner(state):
  for state_slice in state:
    winner_in_slice = slice_winner(state_slice)
    if winner_in_slice != draw_token:
      return winner_in_slice

  state_size = len(state)

  for i in range(state_size):
    state_slice = []
    for j in range(state_size):
      state_slice.append([state[j][i][k] for k in range(state_size)])

    winner_in_slice = slice_winner(state_slice)

    if winner_in_slice != draw_token:
      return winner_in_slice

  diagonals = [0, 0, 0, 0]
  for i in range(state_size):
    diagonals[0] += state[i][i][i]
    diagonals[1] += state[state_size - 1 - i][i][i]
    diagonals[2] += state[i][state_size - 1 - i][i]
    diagonals[3] += state[state_size - 1 - i][state_size - 1 - i][i]

  if (p1_token * state_size) in diagonals:
    return p1_token

  elif (p2_token * state_size) in diagonals:
    return p2_token

  return draw_token


def str_token(cell):
  if cell == p1_token:
    return "X"
  elif cell == p2_token:
    return "O"

  return "."

def draw_board(state):
  result = ""
  state_size = len(state)
  for y in range(state_size):
    for z in range(state_size):
      for x in range(state_size):
        result += str_token(state[x][y][z]) + " "
      result += "\t"
    result += "\n"
  return result


player_1_turn = True
occupied_position = []

def monteCarloAI(board, occupied_position, n_simulation):
    possible_position = {}
    for i in range(n_simulation):
        player_1_turn = False
        first_turn = True
        temp_occupied_position = copy.deepcopy(occupied_position)
        temp_board = copy.deepcopy(board)

        x = np.random.randint(4)
        y = np.random.randint(4)
        z = np.random.randint(4)
        c = 64

        temp_pos = [x, y, z]
        temp_id = str(x)+"," + str(y) + "," + str(z)

        while (temp_pos in temp_occupied_position):
            x = np.random.randint(4)
            y = np.random.randint(4)
            z = np.random.randint(4)
            temp_pos = [x, y, z]
            temp_id = str(x)+"," + str(y) + "," + str(z)

        #init temp_id as a possible possition
        if not (temp_id in possible_position):
            possible_position[temp_id] = 0

        while winner(temp_board) == draw_token and c > 0:
            #simulate a gameplay
            if player_1_turn and not(first_turn):
                [x, y, z] = np.random.randint(4, size = 3)
            elif not(first_turn):
                [x, y, z] = np.random.randint(4, size = 3)

            if temp_board[x][y][z] == draw_token:
                first_turn = False
                temp_occupied_position.append([x,y,z])
                temp_board[x][y][z] = 1 if player_1_turn else -1
                player_1_turn = not player_1_turn
            c += -1

        if winner(temp_board) == 1:
            possible_position[temp_id] += -1
            #print "human sucks"
        elif winner(temp_board) == -1:
            possible_position[temp_id] += + 1
            #print "MATRIX RULES"
        else:
            possible_position[temp_id] += 0
            #print "tie... :("

        #reinit temp_board and temp_occupied_position
        temp_board = []
        temp_occupied_position = []

    #best chance to win
    print possible_position
    idmax =  max(possible_position, key=lambda k: possible_position[k])
    result = map(int, idmax.split(','))
    return result

while winner(board) == draw_token:

  # Print board state
  print ""
  print "Board:"
  print draw_board(board)
  print ""

  # Print
  print "Player %s turn:" % (1 if player_1_turn else 2)

  # Get input for player 1
  if player_1_turn:
      x = int(raw_input("x: "))
      y = int(raw_input("y: "))
      z = int(raw_input("z: "))
  else:
      temp_board = copy.deepcopy(board)
      temp_occupied_position = copy.deepcopy(occupied_position)
      [x, y, z] = monteCarloAI(temp_board, temp_occupied_position, 20000)
      #print "came back from monteCarloAI"

  if board[x][y][z] == draw_token:
    occupied_position.append([x,y,z])
    board[x][y][z] = 1 if player_1_turn else -1
    player_1_turn = not player_1_turn

  else:
    print ""
    print "ERROR: occupied position, please retry in a new position"
    print ""

# Print board state
print ""
print "Board:"
print draw_board(board)
print ""

print "Player %s is the winner!" % (1 if winner(board) == 1 else 2)
