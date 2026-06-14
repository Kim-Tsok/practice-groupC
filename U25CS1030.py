import math

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

discriminant = b**2 - 4*a*c

if discriminant > 0:
    x1 = (-b + math.sqrt(discriminant)) / (2*a)
    x2 = (-b - math.sqrt(discriminant)) / (2*a)
    print("Roots are:", x1, "and", x2)

elif discriminant == 0:
    x = -b / (2*a)
    print("The root is:", x)

else:
    real = -b / (2*a)
    imag = math.sqrt(-discriminant) / (2*a)
    print("Roots are:")
    print(real, "+", imag, "i")
    print(real, "-", imag, "i")
