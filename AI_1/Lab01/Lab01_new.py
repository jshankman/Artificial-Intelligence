#
# Jake Shankman, September 6 2011
#
# Lab01 of Word Ladders... Neighbor Counter
#
#   Input: User input string and dictionary of 6 letter words
# Process: Determine neighbors of input string, if any exist
#  Output: Print out neighbors, with number indicating order found in
#
def allsimilar(word, valid):
  wl = list(word)
  for i, c in enumerate(wl):
    for x in string.ascii_lowercase:
      if x == c: continue
      wl[i] = x
      nw = ''.join(wl)
      if valid(nw): yield nw
    wl[i] = c
        #
#
# end of file
#
