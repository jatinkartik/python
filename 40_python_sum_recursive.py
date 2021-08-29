def sumRecursive(num):
    if(num==1):
        return 1
    return num+sumRecursive(num-1)
    
var = sumRecursive(10)
print(var)

for l in range(5,0,-1):
    print(" * "*l)