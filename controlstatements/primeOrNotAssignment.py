''' 
Loop from 2 to n-1 and assign primeFlag to be false if n%i==0
* if(primeFlag):
    print("Prime number")
else:
    print("Not a prime number")
'''

n = int(input("Enter a number to check if it is prime"))
primeFlag=True

for i in range(2,n):
    if n%i == 0:
        primeFlag=False

if(primeFlag):
    print("Prime")
else:
    print("Not Prime")
    