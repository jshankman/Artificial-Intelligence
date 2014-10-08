#
# Jake Shankman, October 13 2011
#
# Lab05: A* Search
#
#   Input: A file containing neighbors to cities and their coordingates
# Process: Finds the neighbors to create a start to finish path,
#  Output: Either the A* Search of the Uniform Cost search path
#
import math
from time import time
from random import shuffle

def distanceFormula(x1, x2, y1, y2):
  x = math.pow((x2 - x1), 2)
  y = math.pow((y2 - y1), 2)
  d = math.sqrt(x + y)
  return round(d, 0)
 
class Edge:
  def __init__(self, x, y, name):
    self.x = x
    self.y = y
    self.name = name
  def getX(self):
    return self.x
  def getY(self):
    return self.y
  def getName(self):
    return self.name
  def isCalled(self, string):
    if self.name == string:
      return True
    else:
      return False

def findnbrs(city,nlist):
  neighbors=[]
  k=0
  while k<len(nlist):
	  #
      s = nlist[k]
      if city in s:
	i = s.index(city)
	if i == 0:
	  neighbors.append(s[1])
	if i == 1:
	  neighbors.append(s[0])
      k = k+1
  return neighbors
    
stype = raw_input('Uniform Cost or A*?: ')
wlist=open('xy.txt','r').read().split()
edgeList = []
cityNames = []
wlist2 = wlist[:]
for word in wlist:
  data = word.split(',')
  data[1] = int(data[1])
  data[2] = int(data[2])
  x = Edge(data[1], data[2], data[0])
  edgeList.append(x)
  cityNames.append(x.getName())
nlist=open('edge_list.txt','r').read().split()
nlist2 = []
k = 0
while k <len(nlist):
  nlist2.append(nlist[k].split(','))
  k=k+1


        
if stype == 'Uniform Cost':
  print 'Uniform Cost'
  start=raw_input('Starting City: ')
  target=raw_input('Ending City: ')
  city = start
  queue = [[0, start]]
  boolean = 0
  tic = time()
  toc = 0
  distance = 0
  masterlist = {}
  while boolean == 0:
    print len(queue)
    print sum([len(p) for p in queue])
    slist = queue.pop(0)
    print '***',slist
    city = slist.pop()
    if city == target:
      print 'DONE'
      print time() - tic
      slist.append(city)
      print slist
      boolean = 1
    else:
      index1 = cityNames.index(city)
      edge1 = edgeList[index1]
      neighbors=findnbrs(city, nlist2)
      slist.append(city)
      while len(neighbors) != 0:
	looplist = slist[:]
	value = neighbors.pop(0)
	index2 = cityNames.index(value)
	edge2 = edgeList[index2]
	if value not in masterlist or masterlist[value]>distanceFormula(edge1.getX(), edge2.getX(), edge1.getY(), edge2.getY()):
	  masterlist[value] = looplist[0] +distanceFormula(edge1.getX(), edge2.getX(), edge1.getY(), edge2.getY())
	  if value not in looplist and looplist not in queue:
	    d = distanceFormula(edge1.getX(), edge2.getX(), edge1.getY(), edge2.getY())
	    looplist[0] = looplist[0] + d
	    looplist.append(value)
	    queue.append(looplist)
	    queue.sort()
	    
if stype == 'A*':
  print 'A*'
  start=raw_input('Starting City: ')
  target=raw_input('Ending City: ')
  city = start
  queue = [[0,0, start]]
  boolean = 0
  tic = time()
  toc = 0
  distance = 0
  masterlist = {}
  while boolean == 0:
    print len(queue)
    print sum([len(p) for p in queue])
    slist = queue.pop(0)
    print '***',slist
    city = slist.pop()
    if city == target:
      print 'DONE'
      print time() - tic
      slist.append(city)
      slist[0] = 0
      print slist
      boolean = 1
    else:
      index1 = cityNames.index(city)
      edge1 = edgeList[index1]
      neighbors=findnbrs(city, nlist2)
      neighbors.sort()
      slist.append(city)
      while len(neighbors) != 0:
	looplist = slist[:]
	value = neighbors.pop(0)
	index2 = cityNames.index(value)
	edge2 = edgeList[index2]
	if value not in masterlist or masterlist[value] > looplist[1]+distanceFormula(edge1.getX(), edge2.getX(), edge1.getY(), edge2.getY()):
	  masterlist[value] = looplist[1]+distanceFormula(edge1.getX(), edge2.getX(), edge1.getY(), edge2.getY())
	  if value not in looplist and looplist not in queue:
	    d = distanceFormula(edge1.getX(), edge2.getX(), edge1.getY(), edge2.getY())
	    looplist[1] = looplist[1] + d
	    h = distanceFormula(edge2.getX(), edgeList[cityNames.index(target)].getX(), edge2.getY(), edgeList[cityNames.index(target)].getY())
	    looplist[0] =  looplist[1] + h
	    looplist.append(value)
	    queue.append(looplist)
	    queue.sort()
	
  