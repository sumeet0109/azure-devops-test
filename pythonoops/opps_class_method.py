
class Employee:
    increment = 1.5

    def __init__(self, name, salary, dept):
        self.ename = name
        self.esalary = salary
        self.departemnt = dept

    def increase(self):
        self.esalary = int(self.esalary * self.increment )  

    @classmethod
    def changesal(cls, amount):
        cls.increment = amount

emp1 = Employee("sumeet", 100, "IT") 
emp2 = Employee("Rashmi", 200, "software")       

# print(emp1.departemnt)
# print(emp1.esalary, emp1.ename)
# emp1.increase()
# print(emp1.esalary)

print(emp1.esalary)
Employee.changesal(2)
emp1.increase()
print(emp1.esalary)
        
