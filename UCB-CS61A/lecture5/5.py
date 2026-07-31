def apply_twice(f,x):
    return f(f(x))

def square(x):
    return x*x

def make_adder(n):
    def adder(k):
        return n+k
    return adder

def triple(x):
    return 3*x

def compose1(f,g):
    def h(x):
        return f(g(x))
    return h

def curry2(f):
    def g(x):
        def h(y):
            return f(x,y)
        return h
    return g