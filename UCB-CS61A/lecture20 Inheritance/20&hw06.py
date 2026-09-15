class A:
    z = -1
    def f(self,x):
        return B(x-1)

class B(A):
    n = 4
    def __init__(self,y):
        if y:
            self.z = self.f(y)
        else:
            self.z = C(y+1)

class C(B):
    def f(self,x):
        return x

#HW06
class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Nothing left to vend. Please restock.'
    >>> v.add_funds(15)
    'Nothing left to vend. Please restock. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'Please add $10 more funds.'
    >>> v.add_funds(7)
    'Current balance: $7'
    >>> v.vend()
    'Please add $3 more funds.'
    >>> v.add_funds(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.add_funds(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.add_funds(15)
    'Nothing left to vend. Please restock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.add_funds(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    def __init__(self,shelf,price):
        self.product = shelf
        self.price = price
        self.balance = 0
        self.stock = 0

    def vend(self):
        if not self.stock:
            print("'Nothing left to vend. Please restock.'")
        elif self.balance < self.price:
            print(f"'Please add ${self.price-self.balance} more funds.'")
        elif self.balance != self.price:
            self.stock = self.stock - 1
            print(f"'Here is your {self.product} and ${self.balance-self.price} change.'")
            self.balance = 0
        else:
            self.balance = 0
            self.stock = self.stock - 1
            print(f"'Here is your {self.product}.'")

    def add_funds(self,money):
        if not self.stock:
            print(f"'Nothing left to vend. Please restock. Here is your ${money}.'")
        else:
            self.balance+=money
            print(f"'Current balance: ${self.balance}'")

    def restock(self,amount):
        self.stock += amount
        if amount:
            print(f"'Current {self.product} stock: {self.stock}'")
