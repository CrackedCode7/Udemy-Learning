s=input() # by default, end user input is a string
print(s)

s=input("Enter your name:") # input with some prompt
print(s)

i=int(input("Enter an integer number")) # converts user input to int
print(i)
print(type(i))
"""You can also use FLOAT to type cast user input"""

lst=[x for x in input("Enter three numbers separated by space:").split()] 
# split function splits by spaces by default
# pass in (,) to add a delimiter for the end user to separate inputs by
print(lst)

'''You can convert the multiple user inputs to float, int, etc. by 
changing 'x' to float(x) or int(x)'''
