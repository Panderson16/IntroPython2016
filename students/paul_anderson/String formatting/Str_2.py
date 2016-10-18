#!/usr/bin/env python3
strs=(1,2,3,4,5)

def list_numbers(numbers):
	#print (numbers[::])
	n=(len(numbers))
	x=['{:d}']*n
	nlist =  (', '.join(x))
	return '"The numbers are: '+nlist+'"'

my_numbers=list_numbers(strs)
print (my_numbers.format(*strs))
