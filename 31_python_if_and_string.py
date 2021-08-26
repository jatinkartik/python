# var = input("Enter you username : -")
# if(len(var)> 16):
#     print("username cannot be greater than 16 character ")
# else:
#     print("you are good to go, Keep Learning")

##slicing method 
# var1 = input("Enter you full name in pascal notation : - ")
# position = 0
# while var1[position:]:
#     position = position + 1;

# print("length of the full name is : -" ,position)

## Join And Count
var2  = input("Enter you full password i will verify that  : -")

length  = ((var2).join(var2)).count(var2) +1

print("Length of the string is : -",length," verifying the lenght :-",len(var2))