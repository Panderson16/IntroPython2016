__author__ = 'panderson'

"""skips the odd items, change to true for even"""
odd = 1
n=4

def skip(s, odd):
	
	return s[odd::2]
	
def chop(n, s):
    s2=s[(n):-n]
    return skip(s2, 0)


s="Though they share an operator, slicing and indexing have a few important differences:"
print(chop(4, s))

s="123456789101112131415"
print(chop(4, s))

	
		

