#Jake Shankman
#4/23/12
#Period 2
#Lab18: Machine Learning

###Have machine search for memory bank. If not in bank, then create a new file. Play a game. For everymove, generate all 9 "mirror" transformations. If any transformation is in, weight it accordingly.
###Else, add current iteration. Store in .txt file with every line being the board and the following line being its beads. Read in to manipulate. Overwrite it with output streams.
from random import randint
from sys import exit
from traceback import print_exc
globalList = []
globalHash = {}

  

def empty(board):
  count = 0
  for item in board:
    if item == '-':
      count += 1
  return count
  
  
def generate(board, piece):
   #print board
   if empty(board) == 0:
     return
   #
   otherpiece = '-'
   if piece == 'X':
     otherpiece = 'O'
   else:
     otherpiece = 'X'
   #
   square = [8,3,4,1,5,9,6,7,2]
   index = 0
   while index < len(board):
     if board[index] == otherpiece or board[index] == '-': # check, other piece ?
       square[index] = 0
     index += 1
   if check(square) == True:
     return
   #  
   if board.count('-') == 1:
     return
   #
   if ''.join(board) not in globalHash.keys():
     globalHash[''.join(board)] = None
     globalList.append(board)
   else:
     return
   #
   i = 0
   while i < len(board):
    if board[i] != '-':
	i+=1
	continue
    board[i] = piece
    generate(board, otherpiece)
    if i < len(board):
      board[i] = '-'
    i += 1
   return
 

def check(board):
  i = 0
  while i < len(board):
    j = i + 1
    while j < len(board):
      k = j + 1
      while k < len(board):
	if board[i] + board[j] + board[k] == 15:
	  return True
	k +=1
      j += 1
    i += 1
  return False
  
#Check if "knowledge" exists by trying to read: If it fails, do the generate method and output it.
def playGame(mp, knowledge):
  movelist = {}
  piece = 'X'
  otherpiece = 'O'
  i = 0
  board = ['-']*9
  while i < len(board):
    index = -1
    if piece == mp:
      if ''.join(board) in knowledge.keys():
	index = nextMove(knowledge[''.join(board)])
    else:
      index = randint(0,len(board) - 1)
      while board[index] != '-':
	index = randint(0, len(board) - 1)
    if piece == mp:
      movelist[''.join(board)] = index
    board[index] = piece
    temp = piece
    piece = otherpiece
    otherpiece = temp
    square = [8,3,4,1,5,9,6,7,2]
    ind = 0
    while ind < len(board):
      if board[ind] == piece or board[ind] == '-': # check, other piece ?
	square[ind] = 0
      ind += 1
    if check(square) == True:
      i = 9
      if mp == piece:
	return movelist, -1
      else:
	return movelist, 3
    i +=1
  return movelist, 1  
def nextMove(weights):
  if len(weights) == 1:
    return int(weights[0])
  elif len(weights) == 0:
    return randint(0, 8)
  else:
    index = weights[randint(0, len(weights) - 1)]
    return int(index)
  
try:
  k = open('knowledge.txt','r').read().splitlines()
  print "There is knowledge for this game\nPlaying Game Now"
  i = 0
  knowledge = {}
  while i < len(k):
    if k[i + 1] == 'None':
      string = list(k[i])
      empty = []
      j = 0
      while j< len(string):
	if string[j] == '-':
	  empty.append(str(j))
	  empty.append(str(j))
	  empty.append(str(j))
	j = j +1
      k[i + 1] = empty
    else:
      final = []
      for item in k[i + 1]:
	if item.isdigit() == True:
	  final.append(item)
      k[i+1] = final
    knowledge[k[i]] = k[i + 1]
    i += 2
  trials = 0
  mp = 'X'
  op = 'O'
  while trials < 10000:
    result = playGame(mp, knowledge)
    moves = result[0]
    change = result[1]
    if str(change) == '3':
      print 'win'
    elif str(change) == '1':
      print 'draw'
    else:
      print 'lose'
    for key in moves.keys():
      if key in knowledge:
	edit = knowledge[key]
	index = str(moves[key])
	c = 0
	if change > 0:
	  while c < change:
	    edit.append(index)
	    c += 1
	else:
	  if index in edit:
	    edit.remove(index)
	knowledge[key] = edit
    temp = mp
    mp = op
    op = temp
    trials += 1  
  fileK = open('knowledge.txt', 'w')
  for key in knowledge.keys():
    print >> fileK, key
    print >> fileK, knowledge[key]
  fileK.close()
except:
  print_exc()
  print "There is no knowledge of this game!\nGenerating now!"
  board = ['-']*9
  generate(board, 'X')
  fileK = open('knowledge.txt','w')
  for key in globalHash.keys():
    print >> fileK, key 
    print >> fileK, globalHash[key]
  fileK.close()