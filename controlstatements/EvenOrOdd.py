x = int(input("Enter a number:"))

if x==0: # accounts for zero, because zero is neither even nor odd
    print(x,"is zero")
elif x%2 == 0:
    print(x,"is even")
else:
    print(x,"is odd")
