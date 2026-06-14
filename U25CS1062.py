#import cmath

a = int(input("Enter the value of a"))
b = int(input("Enter the value of b"))
c = int(input("Enter the value of c"))

d = b**2 - 4*a*c

sol1 = -b + (d) ** (0.5) / 2 * a
sol2 = -b - (d) ** (0.5) / 2 * a

if d>0:
    print(f"The equation does not have a real root.\n But the answer is {sol1} and {sol2}")

else:
    #sol1 = -b + cmath.sqrt(d)/2*a
    #sol2 = -b - cmath.sqrt(d)/2*a

    print(f"The values of X are {sol1} and {sol2}")