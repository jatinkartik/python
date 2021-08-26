var = input("Enter the number  : -")
var =  int(var)

# for l in range(2,var):
#     if(var%l==0):
#         print("No is not prime")
#         break
# else:
#     print("prime")

def fact(var1):
    if(var1 <=1):
        return 1;
    else:
        return var1*fact(var1-1)

var2 = fact(var)
print(var2)