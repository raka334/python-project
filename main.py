a = input("Enter your email address")
if "@" in a:
    print("Your Have Valid Email  address")
    b = (a.index("@"))
    b = int(b)
    c = a[0:b]
    d = a[b+1:]
    print(c)
    print(d)
