a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

inroot = b**2 - 4*a*c

if inroot >= 0:
    root1 = (-b + inroot ** 0.5) / (2*a)
    root2 = (-b - inroot ** 0.5) / (2*a)
    print("Root 1:", root1)
    print("Root 2:", root2)
else:
    print("No real roots")
