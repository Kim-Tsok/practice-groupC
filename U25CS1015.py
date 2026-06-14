import math

a = 1
b = -4 
c = 4

discriminant = b**2 - 4*a*c
 
firstVal = -b + (math.sqrt(discriminant)) / 2*a
secondVal = -b - (math.sqrt(discriminant)) / 2*a
 
print(f"The root of the equation is {firstVal} or {secondVal}")
