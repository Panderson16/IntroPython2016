l1 = ['test', 'one', 'test', 'one', 'test', 'one']

def dbuild(line, last_word):
	#print('in dbuild')
	for word in line:
		#print (last_word)
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

def new_word(word, next_word):
	#print('in new_word')
	dword.setdefault(word, []).append({next_word: 1})
	#print ('the word is: {}, the value is: {}'.format(word, dword[word]))
	#return dword.setdefault(word, [1, {next_word: 1}])

def update_word(word, next_word):
	print('in update word')
	#temp = dword[word][0]
	count = dword[word][0].get(next_word, 0)
	print ('count is {}'.format(count))
	count+=1

	dword[word][0] = {next_word: count}
	#print ('next_word is: {}'.format(next_word))
	#temp2 = temp[next_word]
	#print('temp2 value is: {}'.format(temp))

last_word=''
dword={}
next_word ={}



dbuild(l1, last_word)
print ('dword is: {}'.format(dword))