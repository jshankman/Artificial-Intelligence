#Jake Shankman
#2/28/12
#Period 2
#Lab15: Schelling's Segregation

import math
from random import randint

def checkerboard():
  board = []
  i = 1
  while i <51:
    row = []
    j = 1
    while j < 51:
      if i % 2 == 0:
	if j %2 == 0:
	  row.append('o')
	else:
	  row.append('x')
      else:
	if j % 2 == 0:
	  row.append('x')
	else:
	  row.append('o')
      j = j +1
    board.append(row)
    i = i + 1
  return board
  

def display(board):
  i = 0
  while i < 50:
    row = board[i]
    print row[:]
    i = i + 1
  print  
    
def delete(board):
  board[0][0] = '-'
  board[0][-1] = '-'
  board[-1][0] = '-'
  board[-1][-1] = '-'
  i = 0
  while i < 750:
    index = randint(1, 50 * 50 - 2)
    r = index / 50
    c = index % 50
    while board[r][c] == '-':
      index = randint(1, 50 * 50 - 2)
      r = index / 50
      c = index % 50
    board[r][c] = '-'
    i = i + 1
  return board
  
def add(board):
  i = 0
  while i < 200:
    index = randint(0, 50 * 50 - 1)
    r = index / 50
    c = index % 50
    while board[r][c] == 'x' or board[r][c] == 'o':
      index = randint(0, 50 * 50 -1)
      r = index / 50
      c = index % 50
    prob = randint(0, 9)
    if prob <= 4:
      board[r][c] = 'x'
    else:
      board[r][c] = 'o'
    i = i + 1
  return board
    
def getneighbors(r, c, board):
  i = -1
  neighbors = []
  while i <= 1:
    j = -1
    while j <= 1:
      if i == 0 and j == 0:
	pass
      elif r + i >= 0 and c + j >= 0 and r + i <50 and c + j <50:
	neighbors.append(board[r + i][c + j])	
      j = j +1
    i = i +1
  return neighbors  
      
def satisfied(neighbors, same):
  if neighbors <= 2 and same >= 1:
    return 'yes'
  elif neighbors > 2 and neighbors <=5 and same >= 2:
    return 'yes'
  elif neighbors > 5 and neighbors <=8 and same >= 3:
    return 'yes'
  else:
    return 'no'
    
def movement(board, row, col, you):
  emptyList = {}
  sat = []
  empty = []
  i = 0
  while i < 50:
    j = 0
    while j < 50:
      if board[i][j] == '-':
	empty.append([i, j])
      j = j +1
    i = i + 1
  for item in empty:
    r = item[0]
    c = item[1]
    n = getneighbors(r, c, board)
    emptyList[str(r) + ' ' + str(c)] = n
  for item in empty:
    r = item[0]
    c = item[1]
    neighbors = emptyList[str(r) + ' ' + str(c)]
    filled = 0
    happiness = 0
    for item in neighbors:
      if item != '-':
	filled = filled + 1
      if item == you:
	happiness = happiness + 1
    satisfaction = satisfied(filled, happiness)
    if satisfaction == 'yes':
      sat.append([r,c])
  if len(sat) == 0:
    index = randint(0, len(empty))
  closest = [row, col]
  mind = 100000
  for item in sat:
    r = item[0]
    c = item[1]
    s1 = (row - r) * (row - r)
    s2 = (col - c) * (col - c)
    d = math.sqrt(s1 + s2)
    if d <= mind:
      mind = d
      closest = [r, c]
  return closest


  
board = delete(checkerboard())
#display(board)
board = add(board)
#display(board)

loop = 0
percent = [-1]*1000
while loop < 1000:
  nList = {}
  i = 0
  while i < 50:
    j = 0
    while j < 50:
      n = getneighbors(i, j, board)
      nList[str(i) + ' ' + str(j)] = n
      j = j + 1
    i = i +1 

#  copy = board[:][:]
  copy = [row[:] for row in board]
  i = 0
  while i < 50:
    j = 0
    while j < 50:
      neighbors = nList[str(i) + ' ' + str(j)]
      you = board[i][j]
      filled = 0
      happiness = 0
      for item in neighbors:
	if item != '-':
	  filled = filled + 1
	if item == you:
	  happiness = happiness + 1
      satisfaction = satisfied(filled, happiness)
      if satisfaction == 'yes':
	copy[i][j] == you
      else:
	move = movement(board, i, j, you)
	row = move[0]
	col = move[1]
	copy[i][j] = '-'
	copy[row][col] = you
      j = j + 1
    i = i + 1
	  
  
  i = 0
  while i < 50:
    j = 0
    while j < 50:
      n = getneighbors(i, j, copy)
      nList[str(i) + ' ' + str(j)] = n
      j = j + 1
    i = i +1 
  
  
  i = 0
  happy = 'yes'
  notempty = 0
  sat = 0
  while i < 50:
    j = 0
    while j < 50:
      neighbors = nList[str(i) + ' ' + str(j)]
      you = copy[i][j]
      filled = 0
      happiness = 0
      if board[i][j] != '-':
	notempty = notempty + 1
	for item in neighbors:
	  if item != '-':
	    filled = filled + 1
	  if item == you:
	    happiness = happiness + 1
	satisfaction = satisfied(filled, happiness)
	if satisfaction == 'yes':
	  sat = sat + 1
	else:
	  happy = 'no'
      j = j +1
    i = i + 1
  percent[loop] = (1.0 * sat)/notempty
  if happy == 'yes':
    print 'Complete Satisfaction Acheived'
    loop = 1000
  
  
  #board = copy[:][:]
  board = [row[:] for row in copy]
  
  loop = loop + 1


for item in percent:
  if item != -1:
    print item


 