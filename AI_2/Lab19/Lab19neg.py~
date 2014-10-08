#Jake Shankman
#4/23/12
#Period 2
#Lab19: Neural Network Negation
from math import *
from random import random
from decimal import *
import sys
def ff(w0, w1, x):
  y = w1*x + w0
  z = 1/(1 + exp(-1 * y))
  return z
  
def negation():
  w0 = random()
  w1 = random()
  
  print 'w0, ' , w0
  print 'w1, ' , w1
  print 'Learning...'
  epoch = 0
  while epoch < 1500:
    
    error = 0.5*(pow(ff(w0,w1,0) - 1, 2) + pow(ff(w0,w1,1) - 0, 2))
    error0 = 0.5*(pow(ff(w0 + 0.01,w1,0) - 1, 2) + pow(ff(w0 + 0.01,w1,1) - 0,2))
    error1 = 0.5*(pow(ff(w0,w1 + 0.01,0) - 1, 2) + pow(ff(w0,w1 + 0.01,1) - 0, 2))
  
    slope0 = (error0 - error)/0.01
    slope1 = (error1 - error)/0.01
  
    w0 -= 0.8 * slope0
    w1 -= 0.8 * slope1
    
    epoch += 1
  print 'Learning Done (1500 epochs)'
  #return w0, w1
  print 'Final w0, ' , w0
  print 'Final w1, ' , w1
  ustr=str(raw_input('Enter 0 or 1: '))
  print ustr
  while ustr == '0' or ustr == '1':
    if ustr == 'q':
      print "Good bye!"
      sys.exit(0)
    elif ustr == '0' or ustr == '1':
      z = ff(w0, w1, int(ustr))
      print 'Result ' , round(z), ' Error ', z
      print
      ustr = str(raw_input('Enter 0 or 1: ' ))

negation()
  