class Employee:
    company = "Tata"
    salary = 55000
    salarybonus = 9000
    @property
    def totalsalary(self):
        return self.salarybonus+ self.salary


var = Employee()
print(Employee.salary)
print(Employee.salarybonus)
print(var.totalsalary)
Employee.salarybonus = 900
print(var.totalsalary)
print(Employee.salarybonus)