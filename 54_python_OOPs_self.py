class Students:
    college = "cu"
    def getCollege(self):
        print(f"Your college is {self.college}")
    def setCollege(self):
        self.college = input("Enter your college name : -")
    @staticmethod
    def welcome():
        print("hey welcome to the college hope your jouney of college will be good ")
var1 = Students()
var1.getCollege()
var1.setCollege()
var1.getCollege()
var1.welcome()
Students.welcome()

