#!/usr/bin/env python3


fruit = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(fruit)
fruit.pop(-1)
print(fruit)
n = input("pick a number between 1 and %s -->" % (len(fruit)))
pop_n=int(n)
fruit.pop(pop_n-1)
print(fruit)
    



