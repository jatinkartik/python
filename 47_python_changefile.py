with open("jatin.txt","r") as file:
    var = file.read()
words = ["bc","mc","bhsdk","kaddu","madr"]
for l in words:	
    var =  var.replace(l,"#&*@(")
    with open("jatin.txt","w") as change:
        change.write(var)
else:
    print("no inappropriate word found in file ")
