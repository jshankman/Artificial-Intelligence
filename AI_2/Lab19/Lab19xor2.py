#Jake Shankman
#Period 2
#6/14/12
#Lab19: Neural Network  XOR
from math import *
from random import random
from decimal import *
import sys

layer1weights = [[random()] * 3, [random()] * 3, [random()] * 3]
layer2weights = [random()]*4
def ff(data, weights):
  y = 0
  k = 0
  while k < len(data):
    y+= data[k]*weights[k]
    k += 1
  z = 1/(1 + exp(-1 * y))
  return z
  

def testCase(x1, x2):
  hiddenLayer = [1]* 4
  k = 0
  while k < len(hiddenLayer) - 1:
    hiddenLayer[k] = ff([x1, x2, 1], layer1weights[k])
    k +=1 
  return ff(hiddenLayer, layer2weights)

def errorCalc():
  return (testCase(0, 0) - 0)**2 + (testCase(0,1) - 1)**2 + (testCase(1, 0) - 1)**2 + (testCase(1,1) - 0)**2
  
epoch = 0
print 'Intial weights: '
print 'Layer1: ', layer1weights
print 'Layer2: ', layer2weights

while epoch < 1500:
  error = errorCalc()
  d1dw = []
  k = 0
  while k < 3:
    d1dw.append([0]*3)
    k += 1

  x = 0
  while x < len(layer1weights):
    y = 0
    while y < len(layer1weights[x]):
      layer1weights[x][y] += 0.01
      error1 = errorCalc()
      d1dw[x][y] = (error1 - error)/0.01
      layer1weights[x][y] -= 0.01
      y += 1
    x += 1
  d2d1 = [0]*4
  x = 0
  while x < len(layer2weights):
    layer2weights[x] += 0.01
    error2 = errorCalc()
    d2d1[x] = (error2 - error)/0.01
    layer2weights[x] -= 0.01
    x += 1
  
  x = 0
  while x < len(d1dw):
    y = 0
    while y < len(d1dw[x]):
      layer1weights[x][y] -= 0.8 * d1dw[x][y]
      y += 1
    x +=1
  
  x = 0
  while x < len(d2d1):
    layer2weights[x] -= 0.8 * d2d1[x]
    x += 1
  
  epoch += 1

print 'Learning Done... 1500 epochs'
print 'Final Layer1Weights: ', layer1weights
print 'Final hidden layer: ', layer2weights

ustr0 = str(raw_input('Value 1 : '))
ustr1 = str(raw_input('Value 2 : '))
while (ustr0 == '0' or ustr0 == '1') and (ustr1 == '0' or ustr1 == '1'):
  if ustr0 == 'q' or ustr1 == 'q':
    print "Good bye!"
    sys.exit(0)
  elif (ustr1 == '0' or ustr1 == '1') and (ustr0 == '0' or ustr0 == '1'):
    print round(testCase(int(ustr0), int(ustr1))), testCase(int(ustr0), int(ustr1))
    ustr0 = str(raw_input('Value 1 : '))
    ustr1 = str(raw_input('Value 2 : '))
