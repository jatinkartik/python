
class Employee():
    country = "India"
    company = "Tata"
    salary = 30000
    def __init__(self):
        print("employee is now detected")

    def getSalary(self):
        print(f"{self.salary}")
    @classmethod
    def getCountry(self):
        print(f"proud to be in {self.country}")

var = Employee()
var.getCountry()
var.country = "NRI"
var.getCountry()
print(Employee.country)
print(var.country)
var.__class__.country = "NRI"
print(Employee.country)
