class Employee:
    company = "Google"
    def getSalary(self, signature):
        print(f"Salary for this employee wkorking in {self.company} is {self.salary}\n{signature}")
    
    @staticmethod
    def greet(): #donot use self under staticmethod
        print("Good Morning, Sir!")

harry = Employee()
harry.salary = 100000
harry.getSalary("Thanks!") #Employee.getSalary(harry)
harry.greet() #Employee.greet()