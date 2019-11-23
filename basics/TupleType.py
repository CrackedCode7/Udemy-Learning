tpl=(40,50,40,'XYZ') #tuples are created with regular brackets
print(tpl)
print(tpl[3]) # indexing
print(tpl*3) # multiplication
print(tpl.count(40)) # will see how many times a value occurs in tuple
print(tpl.index('XYZ'))

tpl2=(40,) # if you want a tuple or list of one element, always have comma after
print(tpl2)

'''You can use all of the functions that you can on a list on a 
tuple as long as they do not MODIFY the tuple'''

lst=[67,34,'ABC']
print(type(lst))
tpl3=tuple(lst) # converts a list to a tuple
print(type(tpl3))
