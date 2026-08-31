def print_all(x):
    print(x)
    return print_all

def print_sums(x):
    print(x)
    def next_sum(y):
        return print_sums(x+y)
    return next_sum

def split(n):
    return n//10,n%10

def sum_digits(n):
    """Return the sum of the digits of postive integer n."""
    if n<10:
        return n
    else:
        all_but_last,last=split(n)
        return sum_digits(all_but_last)+last

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)

def luhn_sum(n):
    if n<10:
        return n
    else:
        all_but_last,last=split(n)
        return luhn_sum_double(all_but_last)+last

def luhn_sum_double(n):
    all_but_last,last=split(n)
    luhn_digit=sum_digits(2*last)
    if n<10:
        return luhn_digit
    else:
        return luhn_sum(all_but_last)+luhn_digit

def identify(n):
    if luhn_sum(n)%10==0:
        return True
    else:
        return False

def sum_digits_rec(n,digit_sum):
    if n==0:
        return digit_sum
    else:
        n,last=split(n)
        return sum_digits_rec(n,digit_sum+last)