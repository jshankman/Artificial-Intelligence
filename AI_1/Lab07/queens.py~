# Torbert, 11.11.2004
#Jake Shankman 10/11/2011: Hill climbing and H calculations
from random import *
from math import *
from sys import *


# handle command line arguments for board dimensions
chessBoard = []
if len(argv) > 1:
	n = int(argv[1])
else:
	n = 8
max = n * (n - 1) / 2

def show(board):
	print
	for r in range(n):
		s = ""
		for c in range(n):
			if (r + c) % 2 == 1:
				s += chr(27) + "[31;46"
			else:
				s += chr(27) + "[31;41"
			s += "m"
			if board[c] == r:
				s += chr(27) + "[1m" + "X"
			else:
				s += " "
		print chr(27) + "[0m" + s + chr(27) + "[0m"
	print chr(27) + "[0m"

def calculateH(board):
 global n
 h = 0
 for r in range(n - 1):
   for c in range(r + 1, n):
     if board[r] == board[c]:
       h = h + 1
     elif abs(board[c] - board[r]) == c - r:
       h = h +1
 return h
def hillClimb(board):
  ##Generate boards by moving all queens to different positions
  ##calculateH and store with boards in a map?
  ##compare for first lowest h and use that as next board. repeat until h = 0. If h never gets to zero, kill program
  gh = calculateH(board)
  best_h = gh
  best_board = board
  global n
  col = 0
  while col < n:
    r = board[col]
    row = 0
    while row < n:
      if r == row:
	pass
      elif r != row:
	temp = board[:]
	temp[col] = row
	h = calculateH(temp)
	if h < best_h:
	  best_h = h
	  best_board = temp
      row = row + 1
    col = col + 1 
  return best_board

def firstChoice(board):
  ##Generate boards by moving all queens to different positions
  ##calculateH and store with boards in a map?
  ##compare for first lowest h and use that as next board. repeat until h = 0. If h never gets to zero, kill program
  nbrs = []
  global n
  col = 0
  while col < n:
    r = board[col]
    row = 0
    while row < n:
      if r == row:
	pass
      elif r != row:
	temp = board[:]
	temp[col] = row
	nbrs.append(temp)
      row = row + 1
    col = col + 1
  shuffle(nbrs)
  k = 0
  while k < len(nbrs):
    if calculateH(nbrs[k]) < calculateH(board):
      break
    k = k+1
  if k >= len(nbrs):
    return board
  else:
    return nbrs[k]

def weight(board):
  ##To determine weight, do calculateH
  # if operation >= 0, put weight at zero, else take abs value
  #take all weights and add up
  nbrs = []
  global n
  col = 0
  while col < n:
    r = board[col]
    row = 0
    while row < n:
      if r == row:
	pass
      elif r != row:
	temp = board[:]
	temp[col] = row
	nbrs.append(temp)
      row = row + 1
    col = col + 1
  k = 0
  total = 0
  while k < len(nbrs):
    h = calculateH(nbrs[k])
    h0 = calculateH(board)
    if h >= h0:
      nbrs[k].insert(0, 0)
    else:
      nbrs[k].insert(0, abs(h - h0))
      total += nbrs[k][0]
    k = k+1
  nbrs.sort()
  k = 0
  problist = []
  while k < len(nbrs):
    prob = nbrs[k][0]
    if prob != 0:
      i = 0
      while i < prob:
	problist.append(nbrs[k][1:])
	i+=1
    k = k + 1
  if len(problist) != 0:
    return problist[int(random() * len(problist) - 1)]
  else:
    return board
    
def generic(pop):
  
  k = 0
  while k < len(pop):
    if len(pop[k]) != 9:
      pop[k].insert(0, calculateH(pop[k]))
    k = k+1
  pop.sort()
  pop = pop[0:6]
  k = 0
  while k < len(pop):
    pop[k] = pop[k][1:]
    k += 1
  k = 0
  lim = len(pop)
  while k < lim:
    children = crossover(pop[k], pop[k + 1])
    pop.append(children.pop(0))
    pop.append(children.pop(0))
    k += 2
  return pop


def crossover(board1, board2):
  r = randint(1, 7)
  child1 = board1[:r] + board2[r:]
  child1 = mutation(child1)
  child2 = board2[:r] + board1[r:]
  child2 = mutation(child2)
  ## DON"T FORGET MUTATIONS FOR THE NEW CHILDREN!!! MAKE A NEW METHOD?
  children = []
  children.append(child1)
  children.append(child2)
  return children

def mutation(board):
  if random() < 0.05:
    board[randint(0, n-1)] = randint(1, n)
  return board
    







def main(success):
	board = range(n)
	for k in range(n):
		board[k] = randint(0, n-1)
	show(board)
	print board
	chessBoard = board
	h = calculateH(board)
	print 'original h', h
	tries = 0
	temp = board[:]
	if type_o_input == 'hillClimb':
	  while tries < 10:
	    temp = hillClimb(temp)
	    tries = tries + 1
	  if calculateH(temp) != 0:
	    print "FAILURE"
	  else:
	    success += 1
	    print "SUCCESS"
	    print temp
	if type_o_input == 'firstChoice':
	   while tries < 10:
	    temp = firstChoice(temp)
	    print calculateH(temp)
	    tries = tries + 1
	   if calculateH(temp) != 0:
	    print "FAILURE"
	   else:
	    success += 1
	    print "SUCCESS"
	    print temp
	if type_o_input == 'weight':
	   while tries < 10:
	    temp = weight(temp)
	    tries = tries + 1
	   if calculateH(temp) != 0:
	    print "FAILURE"
	   else:
	    success += 1
	    print "SUCCESS"
	    print temp
	if type_o_input == 'generic':
	    population = 12
	    pop = []
	    k = 0
	    while k < population:
	      board = range(n)
	      for i in range(n):
		board[i] = randint(0, n-1)
	      board.insert(0, calculateH(board))
	      pop.append(board)
	      k += 1
	    while tries < 1000:
	      pop = generic(pop)
	      tries = tries + 1
	    if calculateH(pop[0]) != 0:
	      print "FAILURE"
	    else:
	      success += 1
	      print "SUCCESS"
	      print pop[0]
	return success
type_o_input = raw_input('Type?:' )
success = 0
k = 0
while k < 1000:
  success = main(success)
  k += 1
print success