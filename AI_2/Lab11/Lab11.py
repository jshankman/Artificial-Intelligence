##Jake Shankman
##AI 2 Period 2
### Lab11 Edge Detection
## 1/24/12


from random import random


#INput kills

def smooth(image,index, x , y, z):
  ##Make Gaussian Smoothing (multiply value by values below)
  ##1  2  1
  ##2  4  2
  ##1  2  1
  ## Average and divide by 16
  indexl = (y*z + x - 1)
  indexr = (y*z + x + 1)
  indexu = ((y - 1)*z + x)
  indexd = ((y+ 1)*z + x)
  
  indexlu = ((y-1)*z + x - 1)
  indexru = ((y-1)*z + x + 1)
  indexld = ((y + 1)*z + x - 1)
  indexrd = ((y + 1)*z + x + 1)
  
  point = int(image[index])
  pvalue = point * 4
  
  pvalue = pvalue + (int(image[indexl]) * 2)
  pvalue = pvalue + (int(image[indexr]) * 2)
  pvalue = pvalue + (int(image[indexu]) * 2)
  pvalue = pvalue + (int(image[indexd]) * 2)
  
  pvalue = pvalue + int(image[indexlu])
  pvalue = pvalue + int(image[indexld])
  pvalue = pvalue + int(image[indexru])
  pvalue = pvalue + int(image[indexrd])
  
  pvalue = pvalue / 16
  print pvalue

def Gx(image, index, x, y, z):
  indexl = (y*z + x - 1)
  indexr = (y*z + x + 1)
  
  indexlu = ((y-1)*z + x - 1)
  indexru = ((y-1)*z + x + 1)
  indexld = ((y + 1)*z + x - 1)
  indexrd = ((y + 1)*z + x + 1)
  
  pvalue = 0
  
  pvalue = pvalue + (int(image[indexl]) * -2)
  pvalue = pvalue + (int(image[indexr]) * 2)
  
  pvalue = pvalue + (int(image[indexlu]) * - 1)
  pvalue = pvalue + (int(image[indexld]) *-1)
  pvalue = pvalue + int(image[indexru]) 
  pvalue = pvalue + int(image[indexrd])
 
  return pvalue
  
  
def Gy(image, index, x, y, z):
  indexu = ((y - 1)*z + x)
  indexd = ((y+ 1)*z + x)
  
  indexlu = ((y-1)*z + x - 1)
  indexru = ((y-1)*z + x + 1)
  indexld = ((y + 1)*z + x - 1)
  indexrd = ((y + 1)*z + x + 1)
  
  pvalue = 0
  

  pvalue = pvalue + (int(image[indexu]) * 2)
  pvalue = pvalue + (int(image[indexd]) * -2)
  
  pvalue = pvalue + int(image[indexlu])
  pvalue = pvalue + (int(image[indexld]) * - 1)
  pvalue = pvalue + int(image[indexru])
  pvalue = pvalue + (int(image[indexrd]) * - 1)
  
  return pvalue
  
task = raw_input()





if task == 'Grayscale':
  s = open('Adventure_Time.ppm','r').read().split()
  print 'P2'
  print s[1]
  print s[2]
  print '255'
  i = 4
  while i < len(s):
    red = int(s[i])
    green = int(s[i + 1])
    blue = int(s[i + 2])
    
    gray = 0.3*red + .59*green + .11*blue
    gray = int(gray + 0.5)
    print gray
    
    i = i + 3

elif task == 'Smooth':
  s = open('Adventure_Time.pgm', 'r').read().split()
  print 'P2'
  print s[1]
  print s[2]
  print '255'
  w = int(s[1])
  h = int(s[2])
  s = s[4:]
  j = 0
  while j < h:
    i = 0
    while i < w:
      x = i
      y = j
      index = int((y*w) + x)
      if x ==0 or x == w - 1 or y == 0 or y == h - 1:
	print s[index]
      else:
	smooth(s, index, x, y, w)
      i = i + 1
    j = j + 1

elif task == 'Edge':
  s = open('Adventure_Time2.pgm', 'r').read().split()
  print 'P2'
  print s[1]
  print s[2]
  print '255'
  w = int(s[1])
  h = int(s[2])
  s = s[4:]
  j = 0
  while j < h:
    i = 0
    while i < w:
      x = i
      y = j
      index = int((y*w) + x)
      if x ==0 or x == w - 1 or y == 0 or y == h - 1:
	print s[index]
      else:
	G = abs(Gx(s, index, x, y, w)) + abs(Gy(s, index, x, y, w))
	if G > 50:
	  print 0
	else:
	  print 255
      i = i + 1
    j = j + 1
