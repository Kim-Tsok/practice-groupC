import math

a = 1
b = 2
c = -1

d = b**2 - 4*a*c

x1 = (-b + math.sqrt(d)) / (2*a)
x2 = (-b - math.sqrt(d)) / (2*a)

print("Root 1 =", x1)
print("Root 2 =", x2)
