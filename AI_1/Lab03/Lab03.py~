#
# Jake Shankman, September 15 2011
#
# Word Ladders Lab03: Ladder Search
#
#   Input: A 6 six letter starting word, a 6 letter ending word and a dictionary of 6 letter words
# Process: Finds all neighbors of word, builds a list of those neighbors,searchs through until a parth to the word is found
#  Output: The word path from start to end and the time it took to run
#
#MAKE A FILE TO PRE GET ALL NEIGHBORS FOR SPEED UP!
import random
from time import time
wlist=open('words.txt','r').read().split()
#
def findnbrs(ustr,wlist):
  neighbors=[]
  k=0
  while k<len(wlist):
	  #
      diff=0
      index=0
      while index<len(ustr):
	      #
	  uletter=ustr[index]
	  word=wlist[k]
	  wletter=word[index]
	  if uletter != wletter:
	      diff=diff+1
	  if diff>1:
	    break
	      #
	  index=index+1
      if diff == 1:
	   neighbors.append(wlist[k])
	  #
	  #
      k=k+1
  return neighbors
#    
stype = raw_input('DFS, BFS or DFSID?: ')
# BREADTH FIRST
if stype == 'BFS':
  print 'Breadth first'
  ustr=raw_input('Statring Word: ')
  target=raw_input('Ending Word: ')
  word = ustr
  queue = [[word]]
  boolean = 0
  tic = time()
  toc = 0
  masterlist = []
  while boolean == 0:
    slist = queue.pop(0)
    print '***',slist
    word = slist.pop()
    neighbors=findnbrs(word, wlist)
    slist.append(word)
    while len(neighbors) != 0:
      looplist = slist[:]
      value = neighbors.pop(0)
      if value not in masterlist:
	masterlist.append(value)
	if value == target:
	  boolean = 1
	  looplist.append(value)
	  queue.append(looplist)
	  toc = time()
	  print looplist
	  print toc - tic
	if value not in looplist and value != target and looplist not in queue:
	  looplist.append(value)
	  queue.append(looplist)


#DEPTH FIRST
if stype == 'DFS':
  print 'Depth first'
  ustr=raw_input('Statring Word: ')
  target=raw_input('Ending Word: ')
  word = ustr
  queue = [[word]]
  boolean = 0
  tic = time()
  toc = 0
  masterlist = []
  while boolean == 0:
    slist = queue.pop()
    print slist
    word = slist.pop()
    neighbors=findnbrs(word, wlist)
    slist.append(word)
    while len(neighbors) != 0:
      looplist = slist[:]
      value = neighbors.pop(0)
     #if value not in masterlist:
      #masterlist.append(value)
      if value == target:
	boolean = 1
	looplist.append(value)
	queue.append(looplist)
	toc = time()
	print looplist
	print toc - tic
	print len(looplist)
      if value not in looplist and value != target and looplist not in queue:
	looplist.append(value)
	queue.append(looplist)

def dfsid(word, target, limit, queue):
  boolean = 0
  masterlist = {}
  while boolean == 0 and len(queue)>0:
    slist = queue.pop()
    print slist
    word = slist.pop()
    neighbors=findnbrs(word, wlist)
    slist.append(word)
    while len(neighbors) != 0:
      looplist = slist[:]
      print len(looplist)
      print limit
      if len(looplist) > limit:
	print "Fail"
	break
      else:
	value = neighbors.pop(0)
	if value == target:
	  boolean = 1
	  looplist.append(value)
	  queue.append(looplist)
	  toc = time()
	  print looplist
	  print len(looplist)
	  print toc - tic
	  return True
	if value not in looplist and value != target:
	  looplist.append(value)
	  queue.append(looplist)
  return False
#DFSIS
if stype == 'DFSID':
  print 'DFSID'
  ustr=raw_input('Statring Word: ')
  target=raw_input('Ending Word: ')
  limit = int(raw_input('Limit?: '))
  word = ustr
  queue = [[word]]
  boolean = 0
  tic = time()
  toc = 0
  if ustr == 'spider':
    while limit <300:
      if dfsid(word, target, limit, queue) == False:
	queue = [[word]]
	limit = limit + 1
      else:
	limit = 300
  else:
    while limit <30:
      if dfsid(word, target, limit, queue) == False:
	queue = [[word]]
	limit = limit + 1
      else:
	limit = 30

# end of file
#