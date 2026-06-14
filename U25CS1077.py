import math
import cmath

def solve_quadratic(a, b, c):
    """
    Solve the quadratic equation ax² + bx + c = 0.
    
    Returns:
        A tuple containing the roots.
        - Two real roots if discriminant > 0
        - One real root (repeated) if discriminant == 0
        - Two complex roots if discriminant < 0
    """
    if a == 0:
        if b == 0:
            if c == 0:
                return "Any real number is a solution (identity equation 0=0)"
            else:
                return "No solution (equation c=0 where c≠0)"
        else:
            # Linear equation
            return (-c / b,)
    
    # Calculate discriminant
    discriminant = b**2 - 4*a*c
    
    if discriminant > 0:
        # Two distinct real roots
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return (root1, root2)
    
    elif discriminant == 0:
        # One real root (repeated)
        root = -b / (2 * a)
        return (root,)
    
    else:
        # Two complex roots
        root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
        root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
        return (root1, root2)


# Interactive main function
def main():
    print("Quadratic Equation Solver: ax² + bx + c = 0\n")
    
    try:
        a = float(input("Enter coefficient a: "))
        b = float(input("Enter coefficient b: "))
        c = float(input("Enter coefficient c: "))
        
        roots = solve_quadratic(a, b, c)
        
        print("\nSolutions:")
        if isinstance(roots, str):
            print(roots)
        elif len(roots) == 1:
            print(f"x = {roots[0]}")
        else:
            print(f"x1 = {roots[0]}")
            print(f"x2 = {roots[1]}")
            
    except ValueError:
        print("Error: Please enter valid numbers.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()