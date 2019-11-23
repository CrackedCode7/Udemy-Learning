''' 
* Ask the user to enter a number
* Display all the numbers up to that number
* skip the multiples of 10
* stop if the number is > 100 
'''

x = int(input("Enter a number greater than 100"))

i=1
while i<x:
    i+=1
    if i>100:
        break
    if i % 10 == 0:
        continue
    print(i)
    