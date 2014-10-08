s=open('circleVote.pgm','r').read().split()
print '\n'.join(s[:4])
data=map(int,s[4:])
maxvotes=max(data)
for k in data:
	print int(0.5+255-255*(1.0*k)/maxvotes)
