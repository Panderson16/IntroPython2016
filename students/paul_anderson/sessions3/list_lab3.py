#!/usr/bin/env python3


fruit = ['Apples', 'Pears', 'Oranges', 'Peaches']
fruit2=fruit[:]

i=0
for fr in fruit2:
    print(fruit)
    print('Do you like %s?' % (fr.lower()))
    n=input('yes or no -->')

    while True:
        if n=='yes' or n=='no':
            break   
        print ('yes or no answers only please')
        print('Do you like %s?' % (fr.lower()))
        n=input('yes or no -->')
    if n=='yes':
        print ("Let's keep those then.")
    else:
        fruit.remove(fruit[i]) 
        print ('Trashing the %s now.' % (fr.lower()))

i+=1          

print(fruit)
    



