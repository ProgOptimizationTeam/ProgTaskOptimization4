def golden_section_method(a, b, e):
    gratio=(((5 ** 0.5) - 1)/2)

    c = b - gratio * (b - a)
    d = a + gratio * (b - a)

    iterations = 0
    
    while abs(b - a) > e:
        if func(c) > func(d):
            a = c
            c = d
            d = a + gratio * (b - a)
        else:
            b = d
            d = c
            c = b - gratio * (b - a)
        optimum = (a + b) / 2
        approx = func(optimum)
        iterations += 1
        # print(f"Root: {optimum}, Function: {approx}, Iterations: {iterations}")
    return optimum, iterations, approx
    

def func(x):
    return (x - 2) ** 2 + 3

def call():
    a = 0
    b = 5
    e = 1e-10
    result, iterations, approx = golden_section_method(0, 5, 1e-4)
    print(f"Root: {result}, Function: {approx}")
