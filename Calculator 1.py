print("Choices: (M)Multiplication, (D)Divistion, (A)Addition, (S)Subtraction, (Sq)Squared and (C)Cubed")

a = input("Select Type: " )

if a == "M":
    x = input("First Number: ")
    y = input("Second Number: ")
    x = float(x)
    y = float(y)
    print("Answer: " +str(x*y))
    
if a == "D":
    z = input("First Number: ")
    q = input("Second number: ")
    z = float(z)
    q = float(q)
    print("Answer: " +str(z//q))

if a == "A":
    k = input("First Number: ")
    m = input("Second Number: ")
    k = float(k)
    m = float(m)
    print("Answer: " +str(k+m))
    
if a == "S":
    d = input("First Number: ")
    c = input("Second Number: ")
    d = float(d)
    c = float(c)
    print("Answer: " +str(d-c))

if a == "Sq":
    e = input("Number: ")
    e = float(e)
    print("Answer: " +str(e*e))

if a == "Cu":
    o = input("Number: ")
    o = float(o)
    l = (o*o)
    print("Answer: " +str(l*l))
