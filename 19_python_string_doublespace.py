var1 = input("Enter your string : - ")
while 1 < var1.count("  ") or var1.count("   "):
    var1 = var1.replace("  ", " ")
    var1 = var1.replace("   "," ")
print(var1)
print("extra spaces is removed ! ")