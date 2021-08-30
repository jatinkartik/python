class Students:
    rollno= 99
    def printroll(self):
        print(self.rollno)
        print("base")

class Teacher(Students):
     def printroll(self):
         print(self.rollno)
         print("derived")

var = Teacher()
var.printroll()
