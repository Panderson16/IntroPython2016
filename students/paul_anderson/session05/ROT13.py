#!/usr/bin/env python

def offset(chars):
    print('in offset')
    i=0
    offset_string=''
    for l in chars:
        if i<13: 
            offset_string=offset_string+(chars[i+13])
        if i>=13:
            offset_string=offset_string+(chars[i-13])
        i+=1
    return offset_string

def encrypt(cl_str):
    for l in cl_str:
        if l.is alpha():
            enc_str=enc_string 
    
low_chars = "abcdefghijklmnopqrstuvwxyz"
up_chars = low_chars.upper()
offset_string = offset(low_chars)+offset(up_chars)
inc_key = list(zip((low_chars+up_chars), offset_string))

print(inc_key)