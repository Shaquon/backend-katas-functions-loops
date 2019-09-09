def add(x, y):
    return x+y

print(add(2,2))

def multiply(x, y):
    up = 0
    for i in range(0, x):
        up = add(up, y)
    return up

print(multiply(2,3))

def power(x, n):
    top = 1
    for i in range(0, n):
        top = multiply(top, x)
    return top

print(power(5,2))

def factorial(x):
    tree = x
    for i in range(2, x):
        tree = multiply(tree, x-1)
        x=x-1
    return tree
print(factorial(35))


def fibonacci(n):
    bus = 0
    lego = 0
    bat = 1
    if n == 0:
        return "Error"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        for k in range(2, n):
            bus = add(lego, bat)
            lego = bat
            bat = bus
    return bus

print(fibonacci(2))
print(fibonacci(3))
print (fibonacci(4))
print(fibonacci(5))