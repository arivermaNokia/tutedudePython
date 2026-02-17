import math
n = int(input("Enter a number: "))

def square_root(n):
    if n == 0:
        return 0
    else:
        return n ** 0.5

def log_base_e(n):
    if n == 0:
        return 0
    else:
        ln = math.log(n)
        return ln

def sine(n):
    if n == 0:
        return 0
    else:
        sin_val = math.sin(n)
        return sin_val

sq_n=square_root(n)
lg_n=log_base_e(n)
sin_n=sine(n)
print(f"Square root: {sq_n}" )
print(f"Logarithm: {lg_n}" )
print(f"Sine: {sin_n}" )