lst=[20,30,40,234]
print(type(lst))
b=bytes(lst) # converts a list into bytes type
print(type(b))

'''Bytes object does not support item assignment. 
Cannot modify it'''

b1=bytearray(lst)
print(type(b1))
b1[2]=33 # you CAN assign values to a bytearray

'''No slicing or repitition can be performed on a byte type Or
a bytearray type'''
