''' Prints numebrs 1 to 20, excluding multiples of three using continue '''

x=0
while x<20:
    x+=1 # increment x by 1
    if x % 3 == 0:
        continue # skips print statement if x is a multiple of 3
    print(x)
    