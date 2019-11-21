x=20
y=30

print((x==20 and y==30)) # only True if both True
print((x==25 and y==30))

print((x==25 or y==30)) # true if at least one is true

print(not(x==25 or y==31)) # true if at least one is NOT true