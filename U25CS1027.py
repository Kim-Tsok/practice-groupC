import cmath

def solve_quadratic():
    print("Quadratic Equation Solver (ax^2 + bx + c = 0)")
    
    try:
        a = float(input("Enter coefficient a: "))
        b = float(input("Enter coefficient b: "))
        c = float(input("Enter coefficient c: "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    if a == 0:
        print("Coefficient 'a' cannot be 0 in a quadratic equation.")
        return

    discriminant = (b**2) - (4 * a * c)

    sol1 = (-b - cmath.sqrt(discriminant)) / (2 * a)
    sol2 = (-b + cmath.sqrt(discriminant)) / (2 * a)

    print("\n--- Results ---")
    
    if discriminant >= 0:
        print(f"The solutions are real numbers: x1 = {sol1.real:.4f} and x2 = {sol2.real:.4f}")
    else:
        print(f"The solutions are complex numbers: x1 = {sol1:.4f} and x2 = {sol2:.4f}")

solve_quadratic()
