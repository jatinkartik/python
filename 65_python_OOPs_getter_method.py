class Employee:
    company = "Tata"
    salary = 55000
    salarybonus = 9000
    @property
    def totalsalary(self):
        return self.salarybonus+ self.salary
    @totalsalary.setter
    def totalsalary(self,val):
        if val < self.salary:
            self.salarybonus = 0
        else:
            self.salarybonus = val - self.salary
        
            

var = Employee()
print(Employee.salarybonus)
print(var.totalsalary)
var.totalsalary = 8000
print(var.salarybonus)
print(var.totalsalary)