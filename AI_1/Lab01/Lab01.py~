#
# Jake Shankman, September 6 2011
#
# Lab01 of Word Ladders... Neighbor Counter
#
#   Input: User input string and dictionary of 6 letter words
# Process: Determine neighbors of input string, if any exist
#  Output: Print out neighbors, with number indicating order found in
#
wlist=open('words.txt','r').read().split()
ustr=raw_input('Statring Word: ')
#
neighbors={}
k=0
key=1
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
        #
    if word != ustr:
        if diff <= 1:
                #
            neighbors[key]=wlist[k]
            key=key+1
                #
	#
    k=k+1
#
if len(neighbors) == 0:
  print 'No known neighbors'
else:
  for key in neighbors.keys():
    #
      print key,":",neighbors[key]
    #
#
# end of file
#
