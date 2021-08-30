
class Person:
    country = "India"
    def __init__(self):
        print("person is now detected")
    def getCountry(self):
        print(f"{self.country}")


class Employee(Person):
    company = "Tata"
    salary = 30000
    def __init__(self):
        super().__init__()
        print("employee is now detected")

    def getSalary(self):
        print(f"{self.salary}")

    def getCountry(self):
        print(f"proud to be in {self.country}")
        return super().getCountry()


class Programmer(Employee):
    company = "Arcesium"
    def __init__(self):
        super().__init__()
        print("freelancer is now detected")

    def getCountry(self):
        return super().getCountry()


var1 = Programmer()
var2 = Employee()
var3 = Person()
var3.getCountry()
var2.getCountry()
var1.getCountry()
print(var1.company)
