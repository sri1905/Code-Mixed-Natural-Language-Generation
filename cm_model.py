import sys
import pickle
from collections import OrderedDict

#starting and ending tags for a sentence
stag = '<s>' 
etag = '<\s>'

def plusone(unit, dic):
	if unit in dic:
		dic[unit]+=1
	else:
		dic[unit]=1

	return dic

def amass(file,data):
	fin = open(file,'r')

	data.append([stag,stag])
	hindi = OrderedDict()
	eng = OrderedDict()

	for line in fin:
		if line=='\n':
			data.append([etag,etag])
			data.append([stag,stag])
		else:
			units = line.split()
			cur = [units[0],units[2]]
			data.append(cur)
			if units[1]=='hi':
				hindi = plusone(units[0],hindi)
			elif units[1]=='en':
				eng = plusone(units[0],eng)

	data.append([etag,etag])
	return data, hindi, eng

def calculate(data, word_cnt, tag_cnt, tagtoword, tw_cnt, n):
	for i in range(len(data)-n+1):

		w_ngram = '' #ngram of words
		t_ngram = '' #ngram of tags

		for c in range(n):
			word = data[i+c][0]
			tag = data[i+c][1]
			
			w_ngram+=word+' '
			t_ngram+=tag+' '

		#print w_ngram, t_ngram
		# tag --> word
		tagram = t_ngram[:-1]
		wordgram = w_ngram[:-1]

		if not tagram in tagtoword:
			tagtoword[tagram] = []
		if not wordgram in tagtoword[tagram]:
			tagtoword[tagram].append(wordgram)
		tag_word = tagram+'<d>'+wordgram
		tw_cnt = plusone(tag_word, tw_cnt)

		word_cnt = plusone(w_ngram[:-1], word_cnt)
		tag_cnt = plusone(t_ngram[:-1], tag_cnt)

	return word_cnt, tag_cnt, tagtoword, tw_cnt

if __name__=="__main__":

	word_cnt = OrderedDict() # structure - {'ngram of words':cnt}
	tag_cnt = OrderedDict() # structure - {'ngram of tags':cnt}

	tagtoword = OrderedDict() # structure - {'ngram of tags' : [ngrams of words]}
	tw_cnt = OrderedDict() # structre - {'tagword':cnt}

	file = raw_input('\nPath to code_mixed data - ')
	#file = 'data/fb_CR.txt'

	data = [] # structure - [[word,tag],[word,tag]...]
	data,hindi,eng = amass(file,data) #reads data from file and adds the start and end tags. File to list.

	# Calculate the frequencies
	for n in range(1,7):
		word_cnt, tag_cnt, tagtoword, tw_cnt = calculate(data, word_cnt, tag_cnt, tagtoword, tw_cnt, n)

	print "Done processing code-mixed data ("+file+')'

	pickle.dump(tag_cnt, open('pickles/cmtag.pkl','wb'))
	pickle.dump(word_cnt, open('pickles/cmword.pkl','wb'))
	pickle.dump(tagtoword, open('pickles/cmtagtoword.pkl','wb'))
	pickle.dump(tw_cnt, open('pickles/cmtw_cnt.pkl','wb'))