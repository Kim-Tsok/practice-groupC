import cmath

def solve_quadratic(a, b, c):
    if a == 0:
        raise ValueError("a (coeficient) cannot be a 0")
    d = (b**2 - (4*a*c))
    
    root1 = (-b + cmath.sqrt(d)) / (2*a) 
    root2 = (-b - cmath.sqrt(d)) / (2*a) 

    return "First root", root1, "Second root", root2

print(solve_quadratic(1, 5, 6))