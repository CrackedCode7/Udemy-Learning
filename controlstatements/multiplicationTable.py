''' Generates a multiplication table from 1-10 for a given user input number '''

x=int(input("Enter a number for generating a table"))

for i in range(1,11): # 1 to 11 so we get the numbers 1-10
    print(x,"X",i,'is equal to',i*x)
