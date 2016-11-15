import pickle
from collections import OrderedDict

Btag = pickle.load(open('pickles/bitag.pkl','rb'))
Mtag = pickle.load(open('pickles/monotag.pkl','rb'))

alltags = OrderedDict()

count = 0
for b in Btag:
	if b in Mtag:
		print b
		count+=1
		v = Btag[b]+Mtag[b]
	else:
		v = Btag[b]

	alltags[b]=v

for m in Mtag:
	if m in Btag:
		v = Mtag[m]+Btag[m]
	else:
		v = Btag[b]

	alltags[m]=v

pickle.dump(alltags, open('pickles/alltags.pkl','wb'))