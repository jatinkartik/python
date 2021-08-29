import random as r 
with open("score.txt","r") as fyl:
    var =  fyl.read()
var = int (var)

def myFunction():
    print("hello")
    randomlist = r.sample(range(100, 10000), 5)
    return randomlist

var2 = myFunction()
if var < var2[0]:
    with open("score.txt","w") as fyle:
        var3 = fyle.write(str(var2[1]))
else:
    print("Existing Score is high Score ")
