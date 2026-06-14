import math

a = 1
b = 3
c = -1

d = (b**2) - (4*a*c)

if d > 0:
  root 1 = (-b + math.sqrt(d)) / (2*a)
  root 2 = (-b - math.sqrt(d)) / (2*a)
  print("root 1:", root 1)
  print("root 2:", root 2)
elif d == 0:
  root = (-b) / (2*a)
  print("the root is:", root)
else:
  print("there are no roots")
  

  


  
