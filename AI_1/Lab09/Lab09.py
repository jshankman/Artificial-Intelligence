#Lab09
#Jake Shankman, Period 2
# November 29, 2011
# 
# INPUT A dictionary of known words to make a tree
# PROCESS Players enter letters, Goes down the tree. Game ends when a person enters a letter who has a child '*' or the letter goes off the tree
# OUTPUT The winner and loser of the game
import random

class Node:
  def __init__(self,val):
    self.val=val
    self.chldrn=[]
  
  def add(self,val):
    child = Node(val[:1])
    #
    if val == '':
      self.chldrn.append(Node('*'))
      return
     # 
    if val[0] == self.val:
      pass
    #
    else:
     isIn = False
     k = 0
     while k < len(self.chldrn):
       if child.val == self.chldrn[k].val and isIn == False:
	 isIn = True
	 node = self.chldrn.pop(k)
	 node.add(val[1:])
	 self.chldrn.append(node)
       k += 1
     if isIn == False:
       child.add(val[1:])
       self.chldrn.append(child)
   
      
      
def display_tree(t,k):
  print '\t'*k,t.val
  for p in t.chldrn:
    display_tree(p,k+1)

def research(node, player, trace):
   print trace
   for child in node.chldrn:
    if child.val != '*':
      if player == 1:
	x, y = research(child, 2, trace+child.val)
	print y
	if x != player:
	  return x, child.val
      else:
	x, y = research(child, 1, trace+child.val)
	print y
	if x != player:
	  return x, child.val
    else:
      if player == 1:
	return 2, '*'
      else:
	return 1, '*'
   if player == 1:
    return '1', (random.choice(node.chldrn)).val
   else:
    return '2', (random.choice(node.chldrn)).val

def main():
  root=Node('*')
  a = open('dictionary.txt','r').read().split()
  for k in a:
    root.add(k)
  display_tree(root,0)
  print root.val
  print map(lambda arg: arg.val,root.chldrn)
  
  #GHOST
  plyAgain = 'yes'
  p1wins = 0
  p2wins = 0
  plyr = 0
  rooty = root
  while plyAgain == 'yes':
    gameOver = False
    root = rooty
    if p1wins == 0 and p2wins == 0:
      plyr = 1
    else:
      plyr = plyr%2 + 1
    string = ''
    star = False
    while gameOver == False and star == False:
     print plyr
     if plyr == 1:
	#MAKE MOVE
	print string, "Player ", plyr, 's turn '
	nxtletter = research(root, plyr, '')
	print nxtletter
	nxtletter = nxtletter[1]
	for k in root.chldrn:
	  if k.val == '*':
	    print 'Word Spelled'
	    star = True
	    plyr = 2
	    break
	if star == False:
	  gameOver = True
	  for c in root.chldrn:
	    if c.val == nxtletter:
	      root = c
	      string += c.val
	      plyr = 2
	      gameOver = False
	      break
	  if gameOver:
	    winner == 2
	    pass
	    string += nxtletter
     elif plyr == 2:
	print string, "Player ", plyr, 's turn '
	nxtletter = research(root, plyr, '')
	print nxtletter
	nxtletter = nxtletter[1]
	for k in root.chldrn:
	  if k.val == '*':
	    print 'Word Spelled'
	    star = True
	    plyr = 1
	    break
	if star == False:
	  gameOver = True
	  for c in root.chldrn:
	    if c.val == nxtletter:
	      root = c
	      string += c.val
	      plyr = 1
	      gameOver = False
	      break
	  if gameOver:
	    winner = 1
	    pass
	    string += nxtletter
	
    print "Word: ", string
    print "Loser: ", plyr
    if plyr == 1:
      print "Winner: ", 2
      p2wins += 1
      print "p1 ", p1wins, " - p2 ", p2wins
    else:
      print "Winner: ", 1
      p1wins += 1
      print "p1 ", p1wins, " - p2 ", p2wins
    plyAgain = (raw_input('Play Again? yes or no?: '))   
main()