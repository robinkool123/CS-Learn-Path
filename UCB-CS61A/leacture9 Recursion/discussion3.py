def swipe(n):
    """Print the digits of n, one per line, first backward then forward.

    >>> swipe(2837)
    7
    3
    8
    2
    8
    3
    7
    """
    if n < 10:
        print(n)
    else:
        all_but_last,last=n//10,n%10
        print(last)
        swipe(all_but_last)
        print(last)

def skip_factorial(n):
    """Return the product of positive integers n * (n - 2) * (n - 4) * ...

    >>> skip_factorial(5) # 5 * 3 * 1
    15
    >>> skip_factorial(8) # 8 * 6 * 4 * 2
    384
    """
    if n==1 or n==2:
        return n
    else:
        return n * skip_factorial(n - 2)

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """


def has_fac(n, d=2):
    if d * d > n:
        return False
    if n % d == 0:
        return True
    else:
        return has_fac(n, d + 1)

def is_prime(n):
    return not has_fac(n)




