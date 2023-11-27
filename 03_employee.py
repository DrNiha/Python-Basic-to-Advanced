class Employee:
    company = "Google"
    salary = 100

harry = Employee()
rajni = Employee()
harry.salary = 3000
rajni.salary = 4000
print(harry.company)
print(rajni.company)
Employee.company = "YouTube"
print(harry.company)
print(rajni.company)
print(harry.salary)
print(rajni.salary)