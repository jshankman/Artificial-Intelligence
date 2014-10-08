black, white, empty, outer = 1, 2, 0, 3
directions = [-11, -10, -9, -1, 1, 9, 10, 11]
corners = [11, 18, 81, 88]
ul = [[11], [12, 21], [13, 22, 31] , [14, 23, 32, 41]]
ur = [[18], [17, 28], [16, 27, 38], [15, 26, 37, 48]]
ll = [[81], [71, 82], [61, 72, 83], [51, 62, 73, 84]]
lr = [[88], [78, 87], [68, 77, 86], [58, 67, 76, 85]]
wall = [13, 14, 15, 16, 31, 41, 51, 61, 83, 84, 85, 86, 38, 48, 58, 68 ]

#LOOK INTO WEDGING, MOBILITY AND AVOIDING UNTRIANGLED CORNERS

from random import choice

def bracket(board, player, square):
	opp = opponent_color(player)
	for d in directions:
		k = square + d
		if board[k] is not opp:
			continue
		while board[k] is opp:
			k = k + d
		if board[k] is player:
			k = k - d
			while k != square:
				board[k] = player
				k = k - d

def would_bracket(board, player, square):
	opp = opponent_color(player)
	for d in directions:
		k = square + d
		if board[k] is not opp:
			continue
		while board[k] is opp:
			k = k + d
		if board[k] is player:
			return True
	return False

def get_legal_moves(board, player):
	possible = []
	for row in range(10, 90, 10):
		for col in range(1, 9):
			square = row + col
			if board[square] is not empty:
				continue
			if would_bracket(board, player, square):
				possible.append(square)
	return possible

def opponent_color(player):
	if player is black: 
		return white
	return black

def search(board, player, ply, best, flag = True):

 #Change from moves to boards
 
 poss=get_legal_moves(board,player)
 if len(poss)==0 or ply > 3:
    return None, hueristic(board, player)
  
 if ply <= 3:
   bestmove = poss[0]
   for move in poss:
     copy = board[:]
     copy[move] = player
     bracket(copy, player, move)
     bestH = search(copy, opponent_color(player), ply + 1, best, False)[1]
     if bestH > hueristic(copy, player):
   
      best = bestH
      bestmove = move

   return bestmove, best
   

 if flag:
   print 'FLAG'
   return best[0]
	

def hueristic(board, player):
  b = 0
  w = 0
  i = 0
  
 
 ##THINGS TO LOOK INTO
 #IF TRIANGLES FAIL, AVOID SURROUNDING CORNERS!!!
 ### WAIT WALLS +2 INSTEAD OF + 1
 
  for triangle in ul:
    for space in triangle:
      if board[space] == player:
	if player == black:
	  b = b + 5
	else:
	  w = w +5
      else:
	break

  for triangle in ur:
    for space in triangle:
      if board[space] == player:
	if player == black:
	  b = b + 5
	else:
	  w = w +5
      else:
	break
  
  for triangle in ll:
    for space in triangle:
      if board[space] == player:
	if player == black:
	  b = b + 5
	else:
	  w = w +5
      else:
	break
  
  for triangle in lr:
    for space in triangle:
      if board[space] == player:
	if player == black:
	  b = b + 5
	else:
	  w = w +5
      else:
	break
	
  while i < 100:
   if i in corners:
     if board[i] == black:
       b = b + 10
     if board[i] == white:
       w = w + 10
   else:
     if board[i] == black:
       b = b + 1
     if board[i] == white:
       w = w + 1
   i = i + 1
 
  if player == black:
    return b - w
  else:
    return w - b
  
  
def pick(board,player):
 poss=get_legal_moves(board,player)
 if len(poss)==0:
    return None

 moves = search(board, player, 1, board)
 if moves[0] == None:
   return choice(get_legal_moves(board, player))
 print moves, '*'
 return moves[0]
