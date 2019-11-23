lst=[10,20,'Evan',-10,30.5] # define a list in square brackets
print(lst)
print(lst[3]) # prints a certain index in the list (0 based)
print(lst[3:5]) # prints a range of elements in a list, similar to slicing in strings
print(lst*4)
print(len(lst))

lst.append(40) # adds an element to a list
lst.remove('Evan') # removes a specific value from a list
del(lst[1]) # deletes an element from a list based on an index
print(lst)

#lst.clear() # removes all elements from a list
#print(lst)

print(max(lst)) # maximum element in a list
print(min(lst)) # minimum element in a list

lst.insert(3,99) # inserts an element at a certain index (3)
print(lst)

lst.sort() # orders the elements in ascending order
print(lst)

lst.sort(reverse=True) # orders the elements in descending order
print(lst)
