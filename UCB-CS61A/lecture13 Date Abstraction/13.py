def mul_rational(x,y):
    return rational(numer(x)*numer(y),denom(x)*denom(y))

def add_rational(x,y):
    return rational(numer(x)*denom(y)+denom(x)*numer(y),denom(x)*denom(y))

def rational(n,d):
    return [n,d]

def numer(x):
    return x[0]

def denom(x):
    return x[1]

def square_rational(x):
    return mul_rational(x,x)

def square_rational(x):
    return rational(numer(x)*numer(x),denom(x)*denom(x))