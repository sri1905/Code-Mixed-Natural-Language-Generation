import pickle
from collections import OrderedDict

print "\nCombining the code-mixed and monolingual tag sequesnces"

Ctag_cnt = pickle.load(open('pickles/cmtag.pkl','rb'))
Mtag_cnt = pickle.load(open('pickles/monotag.pkl','rb'))

Ctw_cnt = pickle.load(open('pickles/cmtw_cnt.pkl','rb'))
Mtw_cnt = pickle.load(open('pickles/monotw_cnt.pkl','rb'))

Ctw = pickle.load(open('pickles/cmtagtoword.pkl','rb'))
Mtw = pickle.load(open('pickles/monotagtoword.pkl','rb'))

#word
Tcnt = OrderedDict()
TtoW = OrderedDict()
TWcnt = OrderedDict()

print "STARTING"

for ct in Ctag_cnt:
	print ct
	if ct in Mtag_cnt:
#BOTH	
		print "\t BOTH"
		v = Ctag_cnt[ct]+Mtag_cnt[ct]#modify this

		for wseq in Mtw[ct]+Ctw[ct]:
			print '\t\t'+wseq
			if ct not in TtoW:
				TtoW[ct] = []
			TtoW[ct].append(wseq)

			key = ct+'<d>'+wseq
			Ccount = 0
			Mcount = 0

			if key in Ctw_cnt:
				Ccount = Ctw_cnt[key]
			if key in Mtw_cnt:
				Mcount = Mtw_cnt[key]
			if not key in TWcnt:
				TWcnt[key] = 0
			TWcnt[key]+=Ccount+Mcount
	else:
#only Code-Mixed
		v = Ctag_cnt[ct]

		for wseq in Ctw[ct]:
			print '\t\t'+wseq
			if ct not in TtoW:
				TtoW[ct]=[]
			TtoW[ct].append(wseq)

			key = ct+'<d>'+wseq
			if key not in TWcnt:
				TWcnt[key]=0
			TWcnt[key]+=Ctw_cnt[key]

	Tcnt[ct] = v

# only mono
print "\t\t\tONLY MONO"
for mt in Mtag_cnt:
	print mt
	if mt not in Ctag_cnt:
		v = Mtag_cnt[mt]
		Tcnt[mt] = v

		for wseq in Mtw[mt]:
			print '\t\t'+wseq
			if mt not in TtoW:
				TtoW[mt]=[]
			TtoW[mt].append(wseq)

			key = mt+'<d>'+wseq
			if key not in TWcnt:
				TWcnt[key]=0
			TWcnt[key]+=Mtw_cnt[key]
		

pickle.dump(Tcnt, open('pickles/All_tag_cnt.pkl','wb'))
pickle.dump(TtoW, open('pickles/All_tagstowords.pkl','wb'))
pickle.dump(TWcnt, open('pickles/All_tagword_cnt.pkl','wb'))