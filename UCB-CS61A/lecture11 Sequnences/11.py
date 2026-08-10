def count(s,value):
    total=0
    for element in s:
        if element==value:
            total+=1
    return total

def same_count(s):
    total=0
    for x,y in s:
        if x==y:
            total+=1
    return total

def sum_below(n):
    sum=0
    for i in range(n+1):
        sum=sum+i
    return sum

def cheer():
    for _ in range (3):
        print('Go Bears!')

def divisors(n):
    return [1]+[x for x in range(2,n) if n%x==0]