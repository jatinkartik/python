var = "hello i am <|name|>, i am from <|place|>"
def changeNameAndPlace(var1,var2,var3):
    var1 = var1.replace("<|name|>",var2)
    var1 = var1.replace("<|place|>",var3)
    return var1
var1 = changeNameAndPlace(var,"jatin","Bijnor")
print(var1)