#!/usr/bin/env/python3

"""
Python exception lab
"""

#response = input('Type something -->')
def safe_input():
    try:
        return input('-->')   
    except (EOFError, KeyboardInterrupt) as the_error:
        print (the_error)
        quit()
        return 'None'

