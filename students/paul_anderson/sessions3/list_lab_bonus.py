#!/usr/bin/env python3


fruit = ['Apples', 'Pears', 'Oranges', 'Peaches']
fruit = fruit*2
running =1
print(fruit)
while running:
    print('This is the fruit we have available.')
    print(fruit)
    print('What fruit would you like to eat?')
    n = input("or type quit to exit -->")
    if n=='quit':
        running = 0
    if n in fruit:
        fruit.remove(n)
    if n not in fruit:
        print ("There is no fruit like that here")   

print(fruit)
    



