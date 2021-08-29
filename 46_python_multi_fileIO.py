print("multiplication  table 2 to 20")

def multiPlicationTable(l):
    var = f"table{l}.txt"
   
    with open(f"./table/{var}","a") as fyle:
        for j in range(10):
            var3 =  l * (j+1)
            fyle.write(f"\n{l}X{j+1}={var3}")
for l in range(2,20):
    multiPlicationTable(l)
        

