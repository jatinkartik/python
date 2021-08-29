word = ["time","python","system","update","mail"]
for l in word:
    
    count = 0
    with open("log.txt","r") as readfile:
        var = readfile.readline()
        while(var):
            count = count+1
            if l in var: 
                print(l," is present at line ", count)
            var = readfile.readline()
