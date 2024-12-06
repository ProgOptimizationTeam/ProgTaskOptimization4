def func(x):
    return -(x ** 2) + 4 * x + 1

def derivative(x):
    return -2*x + 4

def gradient_ascent(x0, a, N):
    x = x0
    for i in range(N):
        x = x + a * derivative(x)
    return x, func(x)

def call():
    x0 = 0
    a = 0.1
    N = 100

    x, f = gradient_ascent(x0, a, N)

    print(f"Root: {x}, Function: {f}")
