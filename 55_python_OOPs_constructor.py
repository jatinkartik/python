class Students:
    college = "cu"

    def __init__(self,college):
        print("hey welcome to the college hope your jouney of college will be good ")
        self.college =  college
    def getCollege(self):
        print(f"Your college is {self.college}")

    def setCollege(self):
        self.college = input("Enter your college name : -")
    

var1 = Students("chandigarh university")
var1.getCollege()
var1.getCollege()
