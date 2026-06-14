#FUNCTION DEFINITION TO USE QUADRATIC FORMULA AND DISPLAY THE VALUES
import cmath
import math

def quad(a, b, c):
    determinant = b**2 - 4*a*c
    if determinant >= 0:
        sqrt_val = math.sqrt(determinant)
    else:
        sqrt_val = cmath.sqrt(determinant)#for negative values
    x1 = (-b + sqrt_val) / (2 * a)
    x2 = (-b - sqrt_val) / (2 * a)
    return x1, x2

# GET INPUT FROM USER
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

x1, x2 = quad(a, b, c)

print(f"The values are {x1} and {x2}")
print(f"The equation can be written as {a}x^2 + {b}x + {c} = 0")