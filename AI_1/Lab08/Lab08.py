#Lab08
#Jake Shankman, Period 2
# November 29, 2011
# 
# INPUT A dictionary of known words to make a tree
# PROCESS Players enter letters, Goes down the tree. Game ends when a person enters a letter who has a child '*' or the letter goes off the tree
# OUTPUT The winner and loser of the game

class Node:
  def __init__(self,val):
    self.val=val
    self.chldrn=[]
  
  def add(self,val):
    child = Node(val[:1])
    #
    if val == '':
      self.chldrn.append(Node('*'))
      self.chldrn.sort()
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
	 self.chldrn.sort()
       k += 1
    if isIn == False:
      child.add(val[1:])
      self.chldrn.append(child)
      self.chldrn.sort()
   
      
      
def display_tree(t,k):
  print '\t'*k,t.val
  for p in t.chldrn:
    display_tree(p,k+1)

      

def main():
  root=Node('*')
  a = open('Lab08.txt','r').read().split()
  for k in a:
    print k
    root.add(k)
  display_tree(root,0)
  
  #GHOST
  players=int(raw_input('Number of Players?: '))
  plyAgain = 'yes'
  p1wins = 0
  p2wins = 0
  while plyAgain == 'yes':
    gameOver = False
    plyr = 1
    winner = 0
    string = ''
    star = False
    while gameOver == False and star == False:
      if plyr == 1:
	#MAKE MOVE
	print string, "Player ", plyr, 's turn '
	nxtletter = raw_input('P1: Next Letter? ')
	for k in root.chldrn:
	  if k.val == '*':
	    print 'Word Spelled'
	    star = True
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
	    string += nxtletter
      elif plyr == 2:
	print string, "Player ", plyr, 's turn '
	nxtletter = raw_input('P2: Next Letter? ')
	for k in root.chldrn:
	  if k.val == '*':
	    print 'Word Spelled'
	    star = True
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