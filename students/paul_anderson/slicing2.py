__author__ = 'panderson'

"""skips the odd items, change to true for even"""
odd = 1

def skip(s, odd):
	
	return s[odd::2]
	
s="Though they share an operator, slicing and indexing have a few important differences:"
print(skip(s, odd))



s="world"
print(skip(s,odd))

	
		

