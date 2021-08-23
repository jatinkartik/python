var1 = "Hello <NAME>, Welcome to our company <XYZ>, \nThank you."
var2 = input("Enter your name : -")
var3 = input("Enter your company name : -")
var1 = var1.replace("<NAME>", var2)
print(var1.replace("<XYZ>", var3))