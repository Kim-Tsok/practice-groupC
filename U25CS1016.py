import math

def almighty_formula(a, b, c):
    discriminant = b**2 - 4*a*c
    
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        print(f"Two real roots: x1 = {x1}, x2 = {x2}")
    elif discriminant == 0:
        x = -b / (2*a)
        print(f"One real root: x = {x}")
    else:
        print("No real roots (discriminant is negative)")

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

almighty_formula(a, b, c)
