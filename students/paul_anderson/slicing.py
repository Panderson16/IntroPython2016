__author__ = 'panderson'

n=''


def exchange(n):
	first = n[0]
	last = n[-1]
	i=1
	l=len(n)-1
	n2=last
	while i<l:
		n2=n2+n[i]
		i+=1

	n2=n2+first
	print (n2)
n="hello"
exchange(n)


n="world"
exchange(n)

	
		

