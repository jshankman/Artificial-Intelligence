#Jake Shankman
#4/23/12
#Period 2
#Lab19: Neural Network Negation
from math import *
from random import random
from decimal import *
import sys
def ff3(w0, w1, x1, w2, x2, w3, x3):
  y = w1*x1 + w0 + x2*w2 + x3*w3
  z = 1/(1 + exp(-1 * y))
  return z
  
def ff2(w0, w1, x1, w2, x2):
  y = w1*x1 + w0 + x2*w2
  z = 1/(1 + exp(-1 * y))
  return z
  
  
def XOR():
  weights = [0]* 3 
  w0 = random()
  w1 = random()
  w2 = random()
  w3 = random()
  print 'w0, ' , w0
  print 'w1, ' , w1
  print 'w2, ' , w2
  print 'w3, ', w3
  print 'Learning...'
  
  epoch = 0
  f = []
  weights[0] = listLearn('s', 's', 's')
  weights[1] = listLearn('s', 's', 's')
  weights[2] = listLearn('s', 's', 's')
  while epoch < 1500:
    i = 0
    while i < 3:
      error = listLearn(weights[i][0], weights[i][1], weights[i][2])
      weights[i] = errorL(weights[i][0], weights[i][1], weights[i][2], w3,error[-1], error[0], error[1], error[2])
      i +=1  
    error = 0.5*(pow(ff3(w0,w1,0, w2, 0, w3, 0) - 1, 2) + pow(ff3(w0,w1,1, w2, 1, w3, 1) - 0, 2))
    error0 = 0.5*(pow(ff3(w0 + 0.01,w1,0, w2, 0, w3, 0) - 1, 2) + pow(ff3(w0 + 0.01,w1,1, w2, 1, w3, 1) - 0,2))
    error1 = 0.5*(pow(ff3(w0,w1 + 0.01,ff2(weights[0][0], weights[0][1], 0, weights[0][2], 0), w2, ff2(weights[0][0], weights[0][1], 0, weights[0][2], 0), w3, ff2(weights[0][0], weights[0][1], 0, weights[0][2], 0)) - 1, 2) + pow(ff3(w0,w1 + 0.01,ff2(weights[0][0], weights[0][1], 1, weights[0][2], 1), w2, ff2(weights[0][0], weights[0][1], 1, weights[0][2], 1), w3, ff2(weights[0][0], weights[0][1], 1, weights[0][2], 1)) - 0, 2))
    error2 = 0.5*(pow(ff3(w0, w1, ff2(weights[1][0], weights[1][1], 0, weights[1][2], 0), w2 + 0.01, ff2(weights[1][0], weights[1][1], 0, weights[1][2], 0), w3, ff2(weights[1][0], weights[1][1], 0, weights[1][2], 0)) - 1, 2) + pow(ff3(w0, w1, ff2(weights[1][0], weights[1][1], 1, weights[1][2], 1), w2 + 0.01, ff2(weights[1][0], weights[1][1], 1, weights[1][2], 1), w3, ff2(weights[1][0], weights[1][1], 1, weights[1][2], 1)) - 0, 2))
    error3 = 0.5*(pow(ff3(w0, w1, ff2(weights[2][0], weights[2][1], 0, weights[2][2], 0), w2, ff2(weights[2][0], weights[2][1], 0, weights[2][2], 0), w3 + 0.01, ff2(weights[2][0], weights[2][1], 0, weights[2][2], 0)) - 1, 2) + pow(ff3(w0, w1, ff2(weights[2][0], weights[2][1], 1, weights[2][2], 1), w2, ff2(weights[2][0], weights[2][1], 1, weights[2][2], 1), w3 + 0.01, ff2(weights[2][0], weights[2][1], 1, weights[2][2], 1)) - 0, 2))
  
    slope0 = (error0 - error)/0.01
    slope1 = (error1 - error)/0.01
    slope2 = (error2 - error)/0.01
    slope3 = (error3 - error)/0.01
  
    w0 -= 0.8 * slope0
    w1 -= 0.8 * slope1
    w2 -= 0.8 * slope2
    w3 -= 0.8 * slope3
     
    epoch += 1
  
  print 'Learning Done (1500 epochs)'
  #return w0, w1
  print 'Final w0, ' , w0
  print 'Final w1, ' , w1
  print "Final w2, ", w2
  print "Final w3, " , w3
  print "Enter XOR Combo: "
  ustr0 = str(raw_input('Value 1 : '))
  ustr1 = str(raw_input('Value 2 : '))
  while (ustr0 == '0' or ustr0 == '1') and (ustr1 == '0' or ustr1 == '1'):
    if ustr0 == 'q' or ustr1 == 'q':
      print "Good bye!"
      sys.exit(0)
    elif (ustr1 == '0' or ustr1 == '1') and (ustr0 == '0' or ustr0 == '1'):
      l = []
      i = 0
      while i < 3:
	#w0, w1, x1, w2, x2
	z = ff2(weights[i][0], weights[i][1], int(ustr0), weights[i][2], int(ustr1))
	l.append(z)
	i += 1
      #w0, w1, x1, w2, x2, w3, x3
      z = ff3(w0, w1, l[0], w2, l[1], w3, l[2])
      print 'Result ' , round(z), ' Error ', z
      print
      print "Enter XOR Combo: "
      ustr0 = str(raw_input('Value 1 : ' ))
      ustr1 = str(raw_input('Value 2 : ' ))
def listLearn(w0, w1, w2):
  if w0 == 's' and w1 == 's' and w2 == 's':
    w0 = random()
    w1 = random()
    w2 = random()
  
  epoch = 0
    
  error = ff2(w0,w1,0, w2, 0)
  error0 = ff2(w0 + 0.01,w1,0, w2, 0)
  error1 = ff2(w0,w1 + 0.01,0, w2, 0)
  error2 = ff2(w0,w1,0, w2 + 0.01, 0)
  
  l = [error0, error1, error2, error]
  return l

def errorL(w0, w1, w2, w3, error, error0, error1, error2):  
  error3 = 0.5*(pow(ff3(w0, w1, error0, w2, error0, w3, error0) - 0, 2) + pow(ff3(w0, w1, error0, w2, error0, w3, error0) - 1, 2))
  error4 = 0.5*(pow(ff3(w0, w1, error1, w2, error1, w3, error1) - 0, 2) + pow(ff3(w0, w1, error1, w2, error1, w3, error1) - 1, 2))
  error5 = 0.5*(pow(ff3(w0, w1, error2, w2, error2, w3, error2) - 0, 2) + pow(ff3(w0, w1, error2, w2, error2, w3, error2) - 1, 2))
  
  slope0 = (error3 - error)/0.01
  slope1 = (error4 - error)/0.01
  slope2 = (error5 - error)/0.01

  w0 -= 0.8 * slope0
  w1 -= 0.8 * slope1
  w2 -= 0.8 * slope2
  l = [w0, w1, w2]
  return l

XOR()
  