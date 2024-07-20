import cmath

def calculate_S1(n):
    total = 0
    for i in range(1, 2*n + 2):
        if i % 2 == 1: 
            total += i
        else: 
            total -= i
    return total

def calculate_S2(n):
    total = 0
    for i in range(1, n + 1):
        total += 1 / i
    return total

def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
    return root1, root2

n=int(input())
print(f"S({n}) = {calculate_S1(n)}")
print(f"S({n}) = {calculate_S2(n)}")

a=int(input())
b=int(input())
c=int(input())
root1, root2 = solve_quadratic(a, b, c)
print(f"Nghiệm của phương trình là x1 = {root1}, x2 = {root2}")

