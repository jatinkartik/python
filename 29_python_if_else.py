var1 = int(input("Enter your age of user 1 : -"))
var2 = int(input("Enter your age of user 2 : -"))
var3 = int(input("Enter your age of user 3 : -"))
var4 = int(input("Enter your age of user 4 : -"))

if var1>var2 and var1>var3 and var1> var4 :
    print(var1 ," is the largest number ")
elif var2> var3 and var2 > var4 :
    print(var2 ," is the largest number ")
elif var3>var4:
    print(var3 ," is the largest number ")
else:
    print(var4 ," is the largest number ")