
class Freelancer:
    company = "freelancer"
    level = "begginer"
class Employee:
    company = "Arcesium"
    ecode = 114
class Programmer(Freelancer,Employee):
    name = "Sahil"


var1 = Programmer()
# var1.company()
print(var1.company)
print(var1.level)
print(var1.ecode)