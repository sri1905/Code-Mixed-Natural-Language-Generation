import sys
import pickle
from collections import OrderedDict

#starting and ending tags for a sentence
stag = '<s>' 
etag = '<\s>'

def add(word, dic):
	if word in dic:
		dic[word]+=1
	else:
		dic[word]=1

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
				add(units[0],hindi)
			elif units[1]=='en':
				add(units[0],eng)

	data.append([etag,etag])
	return data, hindi, eng

def calculate(data, word_cnt, tag_cnt, n):
	for i in range(len(data)-n+1):

		w_ngram = '' #ngram of words
		t_ngram = '' #ngram of tags

		for c in range(n):
			word = data[i+c][0]
			tag = data[i+c][1]
			
			w_ngram+=word+' '
			t_ngram+=tag+' '

		#print w_ngram, t_ngram

		add(w_ngram[:-1], word_cnt)
		add(t_ngram[:-1], tag_cnt)

	return word_cnt, tag_cnt

if __name__=="__main__":

	word_cnt = OrderedDict() # structure - {'ngram of words':[cnt of n,cnt of n-1]}
	tag_cnt = OrderedDict() # structure - {'ngram of tags':[cnt of n,cnt of n-1]}

	#file = raw_input('Enter path to the file - ')
	file = 'code_mixed/fb_CR.txt'

	data = [] # structure - [[word,tag],[word,tag]...]
	data,hindi,eng = amass(file,data) #reads data from file and adds the start and end tags. File to list.

	# Calculate the frequencies
	for n in range(1,7):
		word_cnt, tag_cnt = calculate(data, word_cnt, tag_cnt, n)
		
	pickle.dump(tag_cnt,open('pickles/bitag.pkl','wb'))
	pickle.dump(word_cnt,open('pickles/biword.pkl','wb'))
