# f=open('code_mixed/fb_CR.txt')

# data=f.readlines()



def find_mapping(number):
	f=open('code_mixed/fb_CR.txt')

	d=f.readlines()
	i=0
	data=[]
	temp=[]
	temp.append('<s> <s> <s>') 
	for j in d:
		if j == '\n':
			temp.append('<\s> <\s> <\s>')
			data.append(temp)
			temp=[]
			temp.append('<s> <s> <s>')
		else:
			temp.append(j)	
	data.append(temp)		

	mapping={}
	for x in range(len(data)):
		for i in range(len(data[x])-number):
			w = ''
			for j in range(number):
				w += data[x][i+j].split()[0]
				w += ' '
			w=w.strip()

			p = ''
			for j in range(number):
				p += data[x][i+j].split()[2]
				p += ' '
			p=p.strip()

			if p in mapping:
				if w in mapping[p]:
					mapping[p][w] += 1
				else:
					mapping[p][w] = 1
			else:
				mapping[p]={w:1}	

	for i in mapping:
		temp = 0
		for j in mapping[i]:
			temp += mapping[i][j]

		for j in mapping[i]:
			mapping[i][j]=mapping[i][j]*1.0/temp	

		# print temp

	return mapping		


mapping = find_mapping(2)
for i in mapping:
	print i,mapping[i]








