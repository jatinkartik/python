import os
with open("file1.txt","r") as file1:
    var = file1.read()
print(var)
with open("file3.txt","w") as file3:
    var1 = file3.write(var)
print("file written to another file success")
os.remove("file1.txt")
os.remove("file3.txt")
os.remove("file2.txt")


