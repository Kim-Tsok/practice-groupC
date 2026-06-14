import math

a = 1
b = -5
c = 6

d = (b**2) - (4*a*c)

if d > 0:
    root1 = (-b + math.sqrt(d)) / (2*a)
    root2 = (-b - math.sqrt(d)) / (2*a)
    print("Root 1 is:", root1)
    print("Root 2 is:", root2)
elif d == 0:
    root = -b / (2*a)
    print("The only root is:", root)
else:
    print("No real roots. The roots are complex numbers.")
  
