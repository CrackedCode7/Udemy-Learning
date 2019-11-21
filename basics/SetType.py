s={10,20,30,'XYZ',10,20,10} # create a set with curly braces
print(s) # notice the set removes the duplicates
print(type(s))

s.update([88,99]) # add elements to a set. Notice set has no order (no indexing)
print(s)

s.remove(30) # remove specific elements from a set
print(s)

'''Sets have no order, so you cannot have indexing, repetition,
and slicing because we cannot index values'''

f=frozenset(s) #converts a set into a frozen set
#f.update([20]) cannot update or remove from a frozen set

'''All we can do with a frozen set is navigate through it with a 
for loop. We cannot add anything or substract any elements'''