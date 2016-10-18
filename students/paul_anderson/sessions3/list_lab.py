#!/usr/bin/env python3

n=0
fruit = ['Apples', 'Pears', 'Oranges', 'Peaches']
print (fruit)
add_fruit = input("what other fuit would you like to add? -->")
fruit.append(add_fruit)
print (fruit)
n = input("pick a number between 1 and %s -->" % (len(fruit)))
fruit_number=int(n)
print(fruit[fruit_number-1])
front=['Pom']
fruit = front+fruit
fruit.insert(0, 'Banana')
print (fruit)
for x in fruit:
    #print (x)
    #print (x[0])
    if (x[0]=='P'): print(x)
    



