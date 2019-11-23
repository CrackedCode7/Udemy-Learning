''' Use assert to tell the user an error if the assertion fails '''

x = int(input("Enter a number greater than 10"))
assert x>10, "Invalid number entered" # will fail and display message to user if assertion fails
print("you entered",x)
