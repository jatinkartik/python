class Archi:
    year = 1
    badge = "begginer"
    team = "purple"
    def printData(self):
        print(f"Badge : {self.badge} |  Year : {self.year} |  Team : {self.team} ")
    def setData(self):
        self.year = int(input("Enter how many year you have expieriance in CyberSec : - "))
        var =  input("Enter you current CyberSec Team : ")
        if var == "":
            self.team = "purple"
        else:
            self.team = var
        var1 = input("Enter you current badge in CyberSec : - ")
        if var1 == "":
            self.badge = "begginer"
        else:
            self.badge = var1

Archiver = Archi()
Archiver.printData()
Archiver.setData()
Archiver.printData()
            
