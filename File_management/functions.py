def add(a,b):
    print(f"Sum is {a+b}")

def sub(a,b):
    print(f"Difference is {a-b}")

def mul(a,b):
    print(f"Product is {a*b}")

def div(a,b):
    print(f"Quotient is {a/b}")

x = lambda a,b : a+b
print(x(3,2))