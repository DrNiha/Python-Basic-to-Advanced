class Employee:
    company = "Google"

    def __init__(self, name, salary, subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit
        
        print("Employee is created!")

    def getDetails(self):
        print(f"The name of the employee is {self.name}")
        print(f"The salary of the employee is {self.salary}")
        print(f"The subunit of the employee is {self.subunit}")
    
    def getSalary(self, signature):
        print(f"Salary for this employee wkorking in {self.company} is {self.salary}\n{signature}")
    
    @staticmethod
    def greet(): #donot use self under staticmethod
        print("Good Morning, Sir!")

harry = Employee("Harry", "100000", "YouTube")
# harry = Employee("") ---> This throws an error (missing 3 positional arguments error)
harry.getDetails()