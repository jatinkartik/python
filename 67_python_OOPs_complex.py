class Complex:
    def __init__(self,val,vali):
        self.val = val
        self.vali = vali
    def __add__(self,num):
        sum = self.val +num.val
        sumi = self.vali +num.vali
        return Complex(sum,sumi)
    def __str__(self):
        return f"{self.val} + {self.vali}i"

var = Complex(54,35)
print(var)
var1 = Complex(5456,364)
print(var1)
sum = var1 + var
print(sum)
sum  = sum + var1
print(sum)