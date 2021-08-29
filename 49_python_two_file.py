with open("file1.txt","r") as file1:
    var1 = file1.read()
with open("file2.txt","r") as file2:
    var2 = file2.read()
print(var1)
print(var2)
if var2 == var1:
    print("both file content is sama ")
