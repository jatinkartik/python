print("function to find max of four ")

def maxOfFour(num1,num2,num3,num4):
    if num1>num2 and num1>num3 and num1>num4:
        return num1
    elif num2>num3 and num2 > num4:
        return num2
    elif num3> num4:
        return num3
    else:
        return num4

var1 = maxOfFour(5443,3534,5354,5635)
print(var1)