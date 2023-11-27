class Employees:
    company = "Camel"
    salary = 100
    location = "Delhi"

    # def changeSalary(self, sal):
    #     # self.salary = sal
    #     self.__class__.salary = sal

    @classmethod
    def changeSalary(cls, sal):
        cls.salary = sal

e = Employees()
print(e.salary)
e.changeSalary(455)
print(e.salary)
print(Employees.salary)