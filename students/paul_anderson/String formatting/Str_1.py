#!/usr/bin/env python3

strs=[2, 123.4567, 10000]
print (strs[::])

#x[0] = (str('{:03d}'.format(strs[0])))
#x[1] = ('{:.5}'.format(strs[1]))
#x[2] = ('{:.0e}'.format(strs[2]))

x=((str('{:03d}'.format(strs[0]))), ('{:.5}'.format(strs[1])), ('{:.0e}'.format(strs[2])))