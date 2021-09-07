import math
class Transaction:
    def __init__(self,payment):
        self.payment = payment
    
    def __add__(self,next):
        return self.payment + next.payment
    
    def __mul__(self,next):
        return self.payment * next.payment
    
    def __sub__(self,next):
        return self.payment - next.payment
    
    def __truediv__(self,next):
        return self.payment / next.payment
    
    def __floordiv__(self,next):
        return self.payment // next.payment
    
    def __str__(self):
        return f"{self.payment}"

    def __len__(self):
        return math.log(self.payment,2)  // credit  : - kamal kumar 

pay1 = Transaction(7003377777677)
pay2 = Transaction(439089)
sum = pay1 + pay2
print(sum)
sum = pay1 * pay2
print(sum)
sum = pay1 / pay2
print(sum)
sum = pay1 - pay2
print(sum)
sum = pay1 // pay2
print(sum)
print(pay1)
print(len(str(pay1)))