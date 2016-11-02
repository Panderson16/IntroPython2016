#!/usr/bin/env python3
#if __name__ == '__main__':
from exception import safe_input

def valid_donation(donation):
	try:
		valid = float(donation)
		return True
	except ValueError:
		return False	

def build_donors(): 
	"""Normally the list of donors would be 
	populated by a file or a DB call, but here
	it is going to be a list of tuples"""
	d1=('Fred', [100, 200, 150])
	d2=('Bob', [500, 100, 350])
	d3=('Mark', [900, 400, 750])
	d4=('Luthor', [300, 500])
	d5=('Wade', [100])
	donors=[d1,d2,d3,d4,d5]
	#print(d1[0])
	return (donors)
	
def list_donors(donors):
    for donor in donors:
        print (donor[0])  
    return 
        
def main_menu():
	response=''
	while not response:
		print('would you like to send Thank you letters or run a Report?')
		print("""What would you like to do:
		          
		Print a Report              [R]
		Write a thank you letter    [L]
		Quit                        [Q]""")
		response = safe_input()
		print(response)
		if response.upper() == 'NONE':
		    break
		elif response.upper() == 'L':
		    return 'letter'
		elif response.upper() == 'R':
		    return 'reports'
		elif response.upper() == 'Q':
		    return 'quit'
		else:
		  print('Invalid selection, please try again.')
		  break


		    
def thank_you(donors):
	#print('Thank you')
	response = ''
	while not response:
		print ('Who would you like to send a Thank You letter to?')
		name=input ('Type the name or "list" for list or "quit"-->')
		
		if name.upper() == 'LIST':
			list_donors(donors)
		elif name.upper()=='QUIT':
			return	
		elif name in dlist:
			print('milking existing cash cow')
			donors = existing_donor(name, donors)
			return donors	
		else:
			print ('Booya, new donor')
			donors=new_donor(donors, name)
			return donors

def existing_donor(name, donors):
	print(donors)
	dindex=0
	dlist=list_donors(donors)
	while True:
		print('How much did we milk {} for this time?'.format(name))
		donation = input('-->')
		if valid_donation(donation):
			donation=float(donation)
			print (donation)	
			break
		else:
			print('Enter a dolar amout entered as simple integer')	
	dindex=dlist.index(name)
	donors[dindex].append(donation)
	print_letter(name, donation)
	return 	donors		

def new_donor(donors, name):
	while True:
		print('How much did we milk {} for?'.format(name))
		donation = input('-->')
		if valid_donation(donation):
			donation=float(donation)
			print (donation)	
			break
		else:
			print('Enter a dolar amout entered as simple integer')
	donors.append([name,donation])
	print_letter(name, donation)
	return donors		

def print_letter(name, donation):
	print('Thank you {} for your donation of ${}. Please give us more money'.format(name, donation))
	return

def reports(donors):
	print('{:8}{:>10}{:>10}'.format('Donor', 'Total', 'Average'))
	for donor in donors:
	
		name = donor[0]
		total=0
		dlist = []
		i=0
		for x in donor:
			if valid_donation(x):
				total+=int(x)
				dlist.append(int(x))
				i+=1
		dlist.sort()
		average=total/i	
		print('{:8}{:10.2f}{:10.2f}'.format(name, total, average))
		print('Donation History:')
		print (dlist)

def quit_now():
	quit()

donors=build_donors()
while True:		
	response=main_menu()	

	if response == 'letter':
		donors = thank_you(donors)
		#print(donors)
	elif response == 'reports':
		print('going to reports')
		reports(donors)
	elif response == 'quit': 
		quit()
