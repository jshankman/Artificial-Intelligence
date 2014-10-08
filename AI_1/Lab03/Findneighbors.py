
# Jake Shankman, September 15 2011
#
# Word Ladders Lab03: Ladder Search
#
#   Input: A 6 six letter starting word, a 6 letter ending word and a dictionary of 6 letter words
# Process: Finds all neighbors of word, builds a list of those neighbors,prints in a new text file, neighbors.txt
#  Output: Neighbors.txt file
#
#MAKE A FILE TO PRE GET ALL NEIGHBORS FOR SPEED UP!
import random
from time import time
writer=open('neighbors.txt','w')
wlist=open('words.txt','r').read().split()
neighbors=[]
i=0
while i<len(wlist):
  ustr=wlist[i]
  k=0
  writer.write(ustr)
  writer.write('\n')
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
	      #
	  index=index+1
      if diff == 1:
	   neighbors.append(wlist[k])
	   writer.write(wlist[k])
	   writer. write(' ')
      k=k+1
  i=i+1
writer.close()
#