#!/usr/bin/env python

#if __name__ == '__main__'

s2=set([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
s3=set([3, 6, 9, 12, 15, 18])
s4=set([4, 8, 12, 16, 20])
print(s2)
print(s3)
print(s4)


print ('subset 2 and 3 {}'.format(s3.issubset(s2)))
print ('subset 2 and 4 {}'.format(s4.issubset(s2)))

s=set(['P', 'y', 't', 'h', 'o', 'n'])
s.update(['i'])
s0=frozenset(['m', 'a', 'r', 't', 'h', 'o', 'n'])
print (s)
print (s0)
print(s.union(s0))
print(s.intersection(s0))