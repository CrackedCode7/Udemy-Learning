dict1={1:"John",2:"bob",3:"bill"} # key and value pairs. Any object can be either key/value

'''key and value pairs are separated by a colon'''

print(dict1)
print(dict1.items()) # shows all items with keys and values

k=dict1.keys() # creates a set containing all keys
for i in k: # loop through and display keys
    print(i)

v=dict1.values() # creates a set containing all values
for i in v: # loop through and display keys
    print(i)

print(dict1[3]) # prints a value if you give a key

del dict1[2] # deletes element 2
print(dict1)