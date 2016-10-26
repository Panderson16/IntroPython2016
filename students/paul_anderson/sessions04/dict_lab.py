#!/usr/bin/env python

#if __name__ == '__main__'

desserts = {}
desserts['name']='Chris'
desserts['city']='Seattle'
desserts['cake']='Chocolate'

print(desserts)
desserts['fruit']='Mango'
del desserts['cake']
print(desserts)
print (desserts.keys())
print(desserts.values())
print ('cake' in desserts)
if 'Mango' in desserts.values():
	print ('True')
else:
	print ("False")	


#section 2
desserts = {}
desserts['name']='Chris'
desserts['city']='Seattle'
desserts['cake']='Chocolate'
new_d={}
for k, v in desserts.items():
	t_num=v.count('t')
	new_d[k]='t'*t_num
print (new_d)




