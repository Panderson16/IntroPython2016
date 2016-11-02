l1 = ['This', 'test', 'a', 'test', 'test', ',', 'test', 'test']
l2 = ['a', 'test', 'a', 'test', 'a', 'test']
l3 = ['only', 'needs', '2', 'lines', '.']

def dbuild(line, last_word):
	print('in dbuild')
	i=0
	for word in line:
		print (last_word)
		if last_word:
			if last_word in dword:
				update_word(last_word, word)
				last_word=word	
				#print('true')
			else:
				new_word(last_word, word)
				last_word=word	
				#print('false')		
		last_word=word		
			

def update_word(word, next_word):
	#get the next word dictionary
	print('word is {}, next word is: {}'.format(word, next_word))

	w=dword[word]
	print ('w is: {}'.format(w))
	count=w[0]
	if next_word in w:
		temp=w[nextword]
		temp+=1
		dword[word]=[(count+1), {next_word: count}]
	else:	
		dword[word]=[(count+1), {next_word: 1} ]

	print(w)

def new_word(word, next_word):
	print('in new_word')
	return dword.setdefault(word, []).append([1, {next_word: 1}])
	#return dword.setdefault(word, [1, {next_word: 1}])

last_word=''
dword={}
next_word ={}

dbuild(l2, last_word)
print ('dword is: {}'.format(dword))

