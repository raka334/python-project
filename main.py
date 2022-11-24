# This is Email Slicer Code Generator.
print("Welcome to Email Slicer Generator")
print("Please enter your email address below")
# Here the user will be prompted to enter their email address.
a = input("Enter your email address => ")
# Here is the email address slicing logic comes in if statement.
if "@" in a:
    print("Your Have Valid Email  address")
    b = (a.index("@"))
    b = int(b)
    c = a[0:b]
    d = a[b+1:]
    print("This is Email Username => ", c)
    print("This is Email Domain =>", d)
else:
    print("Invalid Email Address")
