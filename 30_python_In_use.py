var = input("Enter the message here : -")
kindPerson = False
if("hacking technique" in var ):
    kindPerson = True
elif("keep help" in var):
    kindPerson = True
elif("hey stuff" in var):
    kindPerson = True
elif(("bro" in var) or ("brother"in var)):
    kindPerson = True

if(kindPerson == True):
    print("the person texting you is great you can help him ")
else: 
    print("that wil be spammer or hater. Ignore Them")