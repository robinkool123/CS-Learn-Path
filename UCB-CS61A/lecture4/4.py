def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.

    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 3+2, 3-2)
    1
    >>> if_function(3>2, 3+2, 3-2)
    5
    """
    if condition:
        return true_result
    else:
        return false_result 

def cond():
    return True
def true_func():
    print (47)
    return 47
def false_func():
    print (42)
    return 42
print (if_function(cond(),true_func(),false_func()))

"""Genrealization"""

def cube(k):
    return pow(k,3)

def summation(n,term):
    """Sum the first N terms of a sequence .
    
    >>> summation(5,cube)
    225
    """
    total,k=0,1
    while k<=n:
        total,k=total+term(k),k+1
    return total
#这里的term是调用的函数，不用管k的大小，因为k是从1开始取到n的。

def sum_naturals(n):
    """Sum the first Natural number
    
    >>> sum_naturals(5)
    15
    """
    total,k=0,1
    while k<=n:
        total,k=total+k,k+1
    return total

from operator import pow
def sum_cubes(n):
    """Sum the first N cubes of natural numbers
    
    >>> sum_cubes(5)
    225
    """
    total_cubes,k=0,1
    while k<=n:
        total_cubes,k=total_cubes+pow(k,3),k+1
    return total_cubes

from operator import mul
def pi_term(k):
    return 8/mul(4*k-3,4*k-1)

def make_adder(n):
    """Return a function that takes one argumaent
    K and return K+N.
    
    >>> add_three=make_adder(3)
    >>> add_three(4)
    7
    >>> make_adder(6)(3)
    9
    """
    def adder(k):
        return k+n
    return adder
#第一次add_three=make_adder(3)的时候，只是把3给了n
#在内部函数里，变为k+3储存起来，整体打包给add_three，等到下一次给k传入参数后，才可以得出结果。
# 传入外层函数的参数后，在传入内层参数k时就只运行内部函数

def wears_jacket_with_if(temp, raining):
    """
    >>> wears_jacket_with_if(90, False)
    False
    >>> wears_jacket_with_if(40, False)
    True
    >>> wears_jacket_with_if(100, True)
    True
    """
    return temp<60 or raining==True

def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    """
    i=2
    while i<n:
        if n%i==0:
            return False
        else:
            i=i+1
    return True

