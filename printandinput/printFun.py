print()
print('Hello'*3) # basic multiplication of a string

'''You can add \n to add a newline to a string so part of the 
output spans multiple lines'''

print("All the power \n is within you")

a,b=10,20
print(a,b,sep=',') # separator SEP used to define what separates print values
print(a,b,sep='\n')
print(a,b,sep='+++')

name="John"
marks=94.5678

print("Name is",name,"marks are",marks) # one way to print strings together with varibales
print("Name is %s marks are %.2f"%(name,marks)) # %s is a string placeholder, %i integer, %f float
'''Above .2f is used to only display 2 numbers after the decimal'''

# braces with format can also be used as a string placeholder
print("Name is {} marks are {}".format(name,marks))

# You can also use indices in the braces that correspond to order in format
print("Name is {0} marks are {1}".format(name,marks))
