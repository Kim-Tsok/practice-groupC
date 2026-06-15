# Quadratic Equation Solver (Almighty Formula)

import math

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

discriminant = b**2 - 4*a*c

if discriminant >= 0:
    x1 = (-b + math.sqrt(discriminant)) / (2*a)
    x2 = (-b - math.sqrt(discriminant)) / (2*a)

    print("Root 1 =", x1)
    print("Root 2 =", x2)
else:
    print("No real roots")
