#Jake Shankman
#4/10/12
#Period 2
#Lab17: Sudoku

from random import randint
from time import time
import copy

def build(line):
  puz = []
  i = 0
  while i < 9:
    j = 0
    temp = []
    while j < 9:
      temp.append(line.pop(0))
      j = j + 1
    puz.append(temp)
    i = i +1
  return puz

def neighbors(row, col):
  neighbors = []
  i = 0
  while i < 9:
    j = 0
    while j < 9:
      if i == int(row) and j != int(col):
	neighbors.append(str(i) + ' ' + str(j))
      elif i != int(row) and j == int(col):
	neighbors.append(str(i) + ' ' + str(j))
      elif i/3 == int(row)/3 and j/3 == int(col)/3:
	if i != int(row) and j != int(col):
	  neighbors.append(str(i) + ' ' + str(j))
      j = j + 1
    i = i + 1
  return  neighbors   

def allNeigh(puzzle):
  allN = []
  i = 0
  while i < 9:
    j = 0
    temp =[]
    while j < 9:
      temp.append(neighbors(i, j))
      j = j +1
    allN.append(temp)
    i = i + 1
  return allN
def displayPuzzle(puzzle):
  for row in puzzle:
    print row
  print
 
def needToSolve(puzzle):
  empty = []
  i = 0
  while i < 9:
    j = 0
    while j < 9:
      if puzzle[i][j] == '.':
	empty.append(str(i) + ' ' + str(j))
      j = j + 1
    i = i + 1
  return empty
  
  
def assign(puzzle, nList, empty):
  assigned = {}
  possible = {}
  i = 0
  while i < 9:
    j = 0
    while j < 9:
      if puzzle[i][j] != '.':
	assigned[str(i) + ' ' + str(j)] = puzzle[i][j]
	possible[str(i) + ' ' + str(j)] = []
      j = j + 1
    i = i + 1

  i = 0
  while i < 9:
    j = 0
    while j < 9:
      if puzzle[i][j] == '.':
    	possible[str(i) + ' ' + str(j)] = ['1','2','3','4','5','6','7','8','9']
	possible[str(i) + ' ' + str(j)] = possibleNumbers(possible, str(i) +  ' '+ str(j), nList, assigned)
      j = j +1
    i = i + 1
    
  current = '0 0'
  i = 0
  j = 0
  while current in empty:
    if j%8 == 0:
      i = i + 1
      j = 0
    else:
      j = j +1
    current = str(i) + ' ' + str(j)  
  print assignNumber(puzzle,nList,assigned,possible,current)
  #
  # update puzzle from assigned
  #
  i = 0
  while i < 9:
    j = 0
    while j < 9:
      puzzle[i][j] = str(assigned[str(i) + ' ' + str(j)])
      j = j +1
    i = i + 1
    
def possibleNumbers(possible, current, nList, assigned):
  n = []
  row = int(current[0])
  col = int(current[-1])
  i = 0
  while i < 9:
    j = 0
    while j < 9:
      if i == row and j == col:
	n = nList[i][j]
      j = j + 1
    i = i + 1
  numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
  for neighbor in n:
    if neighbor in assigned:
      if assigned[neighbor] in numbers:
	numbers.remove(assigned[neighbor])
  return numbers
  #k = 0
  #finalv = possible[current][:]
  #while k < len(possible[current]):
    #if possible[current][k] not in numbers:
      #finalv.remove(possible[current][k])
    #k = k +1
  #return finalv
  
  
def pickNext(current, possible, assigned):
  lowest = current
  val = 10
  i = 0
  while i < 9:
    j = 0
    while j < 9:
      space = str(i) + ' '+ str(j)
      if space in assigned.keys():
	pass
      elif len(possible[space]) < val and len(possible[space]) >= 0:
	lowest = space
	val = len(possible[space])
      j = j + 1
    i = i + 1
  return lowest
   
def assignNumber(puzzle, nList, assigned, possible, current):
  if len(assigned) == 81:
    return True
  else:
    nextspace = pickNext(current, possible, assigned)
    if nextspace == current:
      return False
    for number in possible[nextspace]:
      assigned[nextspace] = number
      n = neighbors(nextspace[0], nextspace[-1])
#      p = possible.copy()
      for item in n:
	if item in assigned:
	  continue
	possible[item] = possibleNumbers(possible, item, nList, assigned)
      #
      retval=assignNumber(puzzle,nList,assigned,possible,nextspace)
      if retval == True:
	return True
      #
      # undo
      #
      #for item in n:
	#possible[item] = p[item]
      del assigned[nextspace]
      for item in n:
	if item in assigned:
	  continue
	possible[item] = possibleNumbers(possible, item, nList, assigned)
      #
    #del assigned[nextspace]
  return False
    
    
def solvePuzzle():
  puzzle = []
  ustr=raw_input('Which File?: ')
  blueprint=open(ustr,'r').read().split()
  number = 1
  tic = time()
  while len(blueprint) > 0:
    print 'Puzzle #' + str(number) 
    puzzle = build(list(blueprint.pop(0)))
    nList = allNeigh(puzzle)
    empty = needToSolve(puzzle)
    #displayPuzzle(puzzle)
    print "Now to solve..."
    assign(puzzle, nList, empty)
    displayPuzzle(puzzle)
    number = number + 1
    print 'Overall Time: ' + str(time() - tic)
	 
  
solvePuzzle()Java