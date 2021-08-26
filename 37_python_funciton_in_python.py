marks = [50, 50, 50, 50, 50]
marks.append(88)
marks.sort()
print(marks)
marks.reverse()
print(marks)

# var = (sum(marks)/(len(marks)*100))*100
# print(len(marks))
# print(var)
def sumvar(var1="User",var2=" "):
    return "Hello "+var1+var2


var3 = sumvar("jatin ","kartik")
var4 = sumvar()
print(var4)
print(var3)

def markssum(mark):
    length = len(marks)
    sum = 0
    for l in range(length):
        sum = sum + mark[l]

    return sum


print(markssum(marks))
