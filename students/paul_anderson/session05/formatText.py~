#!/usr/bin/env python

import random

def open_txt(a_file):
   with open(a_file, encoding='utf8') as work_file:
      for a_line in work_file:
         current_line=line_dict(a_line)
         full_text.extend(current_line)


def line_dict(txt_line):
   current_line='{}'.format(txt_line.rstrip())
   sp_line = current_line.split(' ')
   new_line=[]
   for word in sp_line:
      word = word.lower() 
      if ',' in word:
         new_line.append(word[0:-1])
         new_line.append(',')
      elif '.' in word:
         new_line.append(word[0:-1])
         new_line.append('.')	
      else:
         new_line.append(word)	
   return new_line	

def zipit(text_list):
    next_word=text_list[2:]
    key_words=list(zip(text_list[0:], text_list[1:]))
    return (dict(zip(key_words, next_word)))

def build_text(trig_dict):
    starting_words = (random.choice(list(zipped_text.keys())))
    i=0
    print ('starting words {}'.format(starting_words))
    first=starting_words[0]
    next = starting_words[1]
    new_text = '{} {}'.format (first.title(), next)
    #print (zipped_text[('out', 'that')])
    for i in range(50):
        key = (first, next)
        #print (key)
        new_text = new_text+' {}'.format(zipped_text[key])
        first = next
        next = zipped_text[key]
        i+=1
    print (new_text)    
        
full_text = []
txt_dict = open_txt('sherlock.txt')
zipped_text = dict(zipit(full_text))
#print(zipped_text)
#starting_words = (random.choice(list(zipped_text.keys())))
build_text(zipped_text)



	