#Jake Shankman
#3/19/12
#Period 2
#Lab16: Map Coloring

from random import randint

class State:
  def __init__(self, name):
    self.name = name
    self.neighbors = []
    self.color = '-'
  def getName(self):
    return self.name
  def setColor(self, color):
    self.color = color
  def getColor(self):
    return self.color
  def addNeighbor(self, n):
    self.neighbors.append(n)
  def getNeighbors(self):
    return self.neighbors
  
def findstate(name, statelist):
  for item in statelist:
    if item.getName() == name:
      return item
  
def findneighbors(state, textlist, statelist):
  k = 0
  while k < len(textlist):
    pair = textlist[k]
    if state.getName() in pair:
      s = pair.split()
      if s[0] != state.getName():
	n = findstate(s[0], statelist)
	inside = False
	for neigh in state.getNeighbors():
	  if neigh.getName() == n.getName():
	    inside = True
	if not inside:
	  state.addNeighbor(n)
      if s[1] != state.getName():
	n = findstate(s[1], statelist)
	inside = False
	for neigh in state.getNeighbors():
	  if neigh.getName() == n.getName():
	    inside = True
	if not inside:
	  state.addNeighbor(n)
    k = k + 1
    
def assign(current, statelist):
  assigned = {}
  possible = {}
  for item in statelist:
    if item == current:
      possible[item] = ['red']
    else:
      possible[item] = ['red', 'blue', 'yellow', 'green']
  assigned[current] = 'red'
  n = current.getNeighbors()
  for item in n:
    possible[item] = ['blue', 'yellow', 'green']
  current.setColor('red')
  assignColor(current, assigned, possible)
 
def pickNext(current, possible, assigned, statelist):
  lowest = current
  val = 4
  for item in statelist:
    if item in assigned:
      pass
    elif len(possible[item]) < val and len(possible[item]) > 0:
      lowest = item
      val = len(possible[item])
  return lowest    

def possibleColors(current, possible):
  n = current.getNeighbors()
  colors = ['red', 'blue', 'yellow', 'green']
  for item in n:
    if item.getColor() in colors:
      colors.remove(item.getColor())
  finalv = possible[current]
  k = 0
  while k < len(possible[current]):
    if possible[current][k] not in colors:
      finalv.remove(possible[current][k])
    k = k +1  
  return finalv
  
def assignColor(current, assigned, possible):
  print 'current', current.name
  if len(assigned) == len(statelist):
    return True
  else:
    nextregion = pickNext(current, possible, assigned, statelist)
    print nextregion.name, possible[nextregion]
    if nextregion.getName()==current.getName():
      return False
    for color in possible[nextregion]:
      assigned[nextregion] = color
      if nextregion.name == 'MD':
	assigned[nextregion] = 'red'
	nextregion.setColor('red')
      if color == current.getColor():
	pass
      else:
	nextregion.setColor(color)
	assigned[nextregion] = color
	print assigned[nextregion], nextregion.name
	n = nextregion.getNeighbors()
	for item in n:
	  possible[item] = possibleColors(item, possible)
	  if len(possible[item]) == 0:
	    print 'Broken', item.name
	retval=assignColor(nextregion, assigned, possible)
	if retval==True:
	  return True
    print nextregion.getName()
    del assigned[nextregion]
  return False
      
def sameColor(statelist):
  for item in statelist:
    neigh = item.getNeighbors()
    for n in neigh:
      if item.getColor() == n.getColor():
	return True
  return False
  
seen = []
statelist = []
textlist = open('states_48.txt','r').read().split('\n')
states = open('states_48.txt','r').read().split()
for item in states:
  if item not in seen:
    seen.append(item)
    statelist.append(State(item))
k = 0
while k < len(statelist):
  findneighbors(statelist[k], textlist, statelist)
  k = k + 1

print
assign(statelist[0], statelist)
  
  

k = 0
while k < len(statelist):
  string = statelist[k].getName() + ' ' + statelist[k].getColor() + ' ['
  n = statelist[k].getNeighbors()
  for obj in n:
    string = string + obj.getName() + ' ' + obj.getColor() + ', '
  string = string[0:-2] + ']'
  print string
  k = k + 1
count = 0
for item in statelist:
  if item.color != '-':
    count += 1
print count, 'count'
print 'Any matches? ',sameColor(statelist)  