def delay(arg):
    """
    >>> delay(delay)()(6)()
    delayed
    delayed
    6
    >>> print(delay(print)()(4))
    delayed
    4
    None
    """
    print('delayed')
    def g():
        return arg
    return g

def trace1(fn):
    def traced(x):
        print('Calling',fn,'on argument',x)
        return fn(x)
    return traced

def pirate(arggg):
    print ('matey')
    def plunder(arggg):
        return arggg
    return plunder

@trace1
def square(x):
    return x*x

def horse(mask):
    horse=mask
    def mask(horse):
        return horse
    return horse(mask)

mask=lambda horse:horse(2)
#mask的作用是传入一个对2操作的函数
#house(mask)，先在house这个函数中传入mask，把外层打开，house=mask使house变成了全局lambda
#然后house(mask)调用lambda，mask(2),得到2

def remove(n,digit):
    """Return all digit of non-negative N
    that are not DIGIT,for some 
    non-nagative DIGIT less than 10.
    >>> remove(231,3)
    21
    >>> remove(243132,2)
    4313
    """
    kept,digits=0,0
    while n>0:
        n,last=n//10,n%10
        if last!=digit:
            kept=10**digits*last+kept
            digits=digits+1
    return kept

@trace1
def sum_square_up_to(n):
    k=1
    total=0
    while k<=0:
        total,k=total+square(k),k+1
    return total


