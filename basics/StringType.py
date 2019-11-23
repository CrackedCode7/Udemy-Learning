s=" You are awesome "
print(s)

s1='''You are
the creator of
your destiny'''
print(s1)

#Indexing a string (zero-based, goes from 0 to length -1)
print(s[0])

#Repitiion of a string
print(s*2)

#Length of a string (or other data types)
print(len(s1))
print(len(s))

#String slicing (does not include element at ending index)
print(s[0:5])
print(s[2:]) # starts at third element and goes to end
print(s[:8]) # goes from start to element BEFORE the element at index 8
print(s[-3:-1]) # starts at the index three from the end and stops at the element before the ending index

#Passing a step value (by default step value is 1)
print(s[0:9:2]) # alternates characters
print(s[15::-1]) # reverses string order
print(s[::-1]) # also reverses string order but without knowing length

print(s.strip()) # strip removes leading and ending spaces
print(s.lstrip()) # strips only leading spaces
print(s.rstrip()) #strips only ending spaces

print(s.find('awe',0,len(s))) # prints the index where awe starts
print(s.find('awe',0,8)) # prints -1 because awe is not found within these indexes
print(s.count("a")) # counts the number of occurences of a substring
print(s.replace("awesome","super"))

print(s.upper()) # prints the string in all upper case.
print(s.lower()) # prints the string in all lower case.
print(s.title()) # prints the string as if it were a title.
