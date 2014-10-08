import random
import string

def research(node, player, trace, choices, flag=True):
   print 'choices',choices
   for child in node.chldrn:
    if child.val != '*':
      if player == 1:
	x, y = research(child, 2, trace+child.val, choices, False)
	if flag:
	  if child.val not in choices:
	    choices.append(child.val)
	elif x != player:
	  return x, child.val
      else:
	x, y = research(child, 1, trace+child.val, choices, False)
	if flag:
	  if child.val not in choices:
	    choices.append(child.val)
	elif x != player:
	  return x, child.val
    else:
      if player == 1:
	return 2, '*'
      else:
	return 1, '*'
   if len(choices) != 0:
     return player%2 + 1, random.choice(choices)
   if player == 1 and len(node.chldrn) != 0:
     return '1', (random.choice(node.chldrn)).val
   elif player == 2 and len(node.chldrn) != 0:
     return '2', (random.choice(node.chldrn)).val
   print '*****'
   return player, random.choice(string.letters)