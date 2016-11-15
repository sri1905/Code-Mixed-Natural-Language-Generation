import sys
import pickle
from random import randint
from operator import itemgetter

alltags = pickle.load(open('pickles/alltags.pkl','rb'))
#words = pickle.load(open('pickle/biword.pkl','rb'))

limit = input('Length of tag sequence - ')

choice = []
seq = []
seq.append('<s>')

while len(seq)<limit:

	l = len(seq)
	if l>6:
		r = randint(1,6)
	else:
		r = randint(1,l)

	lhs = ''	
	for i in range(l-r,l):
		lhs+=seq[i]+' '

	#print seq
	#print '\t'+str(r)+':'+lhs

	R_lim = r+1
	for t in alltags:
		l = len(t.split())

		if l>R_lim:
			break

		elif l==R_lim:

			rhs = ''
			for i in range(l-1):
				rhs+=t.split()[i]+' '
			
			#print t+'\t'+rhs

			if lhs==rhs:
				#print '\tmatched'
				choice.append((t.split()[l-1],alltags[t]))

			if len(choice)>10:
				choice.sort(key=itemgetter(1))
				#print choice
				choice.remove(choice[0])

	#print choice
	r = randint(0,9)
	#print choice[r][0]
	seq.append(choice[r][0])
	print seq


