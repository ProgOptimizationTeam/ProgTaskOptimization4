def bisection_method(func, a, b, tol):
    
    if func(a) * func(b) >= 0:
        print("Function values at the interval endpoints must have opposite signs.")
        if func(a) == 0:
            return a, 0
        else:
            return b, 0
    print(f"{'Iteration':<10} {'a':<10} {'b':<10} {'c':<10} {'f(c)':<10}")
    print("-" * 50)
    iterations = 0
    while True:
        c = (a + b) / 2  
        fc = func(c)
        print(f"{iterations:<10} {a:<10.6f} {b:<10.6f} {c:<10.6f} {fc:<10.6f}")
        if abs(fc) < tol: 
            return c, iterations
        
        if func(a) * fc < 0:
            b = c 
        else:
            a = c  
        
        iterations += 1
    
def func(x):
    return x**3 - 6*x**2 + 11*x - 6

# Test the implementation
if __name__ == "__main__":
    a = 1
    b = 2
    tol = 1e-6
    root, iters = bisection_method(func, a, b, tol)
    print(f"Root: {root}, Iterations: {iters}")