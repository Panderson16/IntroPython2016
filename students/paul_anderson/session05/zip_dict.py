#!/usr/bin/env python

text_list = [('word %i'%i) for i in range(10)]

def zipit(text_list):
    next_word=text_list[2:]
    key_words=list(zip(text_list[0:], text_list[1:]))
    return (dict(zip(key_words, next_word)))

trig_dict = zipit(text_list)
print (trig_dict)



        
    
	