#!/usr/bin/env python

#if __name__ == '__main__'

def line_dict(txt_line):
	current_line='{}'.format(txt_line.rstrip())
	sp_line = current_line.split(' ')
	new_line=[]
	i=0
	for item in sp_line:
		if ',' in item:
			i+=1
			new_line.append(item[0:-1])
			new_line.append(',')
		elif '.' in item:
			i+=1
			new_line.append(item[0:-1])
			new_line.append('.')
		else:
			new_line.append(item)	
		i+=1
	#print (new_line)
	return new_line	


def open_txt(a_file):
	with open(a_file, encoding='utf8') as work_file:
		line_number=0
		prev_line=[]
		last_word=''
		current_line=[]
		for a_line in work_file:
			current_line=line_dict(a_line)
			#print(current_line)
			dbuild(current_line, last_word)
			
def dbuild(line, last_word):
	#print('in dbuild')
	for word in line:
		#print (last_word)
		word=word.lower()
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
	dword.setdefault(word, []).append({next_word: 1})
	word_count[word]=1


def update_word(word, next_word):
	count = dword[word][0].get(next_word, 0)
	count+=1
	dword[word][0][next_word] = count
	word_count[word]+=1
			

last_word=''
dword={}
next_word ={}
word_count={}
open_txt('test.txt')
print (dword)
#print ('dword sherlock is: {}'.format(dword['sherlock']))
print (word_count)


