# string type in python

var1 = "this is 1st type string in which we can add single quote like this jatin's laptop"
var2 = 'this is 1st type string in which we can add doubel quote like this jatin" phone'
var3 = '''          this is also a type of string
             in which we can add anythin like jatin's
          laptop and jatin"s phone '''
var4 = input("Enter the value of string: - ")
print(var1+var2+var3+var4)
print(var4[0],var4[1],var4[2],var4[3],var4[4])
# sting slicing is showed like this 
print(var4[0:5])
print(var4[-6:])
print(var4[::2]) #print whole string with excape value of 2 that means every2nd character is print
print(var4.__len__())
print(var4.endswith("tyagi"))
print(var4.count("o"))
print(var4.capitalize())
print(var4.find("tyagi"))
print(var4[10])
print(var4.replace("jatintyagi", "jatinkartik"))
print('hello\'') 