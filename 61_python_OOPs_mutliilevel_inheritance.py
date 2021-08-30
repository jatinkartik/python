class Person:
    country = "India"
    def getCountry(self):
        print(f"{self.country}")
class Employee(Person):
    company = "Tata"
    salary = 30000
    def getSalary(self):
        print(f"{self.salary}")
    def getCountry(self):
        print(f"proud to be in {self.country}")
class Programmer(Employee):
    company = "Arcesium"

var1 = Programmer()
var2 = Employee()
var3 = Person()

var3.getCountry()
var2.getCountry()
var1.getCountry()
print(var1.company
)