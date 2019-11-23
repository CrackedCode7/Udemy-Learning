''' For loop that breaks when a certain number in a list is found '''

lst = [3,6,5,9,12]

for i in lst:
    if i == 5: # break the loop if 5 is in the list
        break
    print(i)

    ''' Break always breaks out of the enclosing looping statement '''
    