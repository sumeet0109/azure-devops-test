
class Employee:

    increment = 1.5
    def __init__(self, name, salary, dept):
        self.ename = name
        self.esalary = salary
        self.departemnt = dept

    def increase(self):
        self.esalary = int(self.esalary * self.increment )    

emp1 = Employee("sumeet", 100, "IT") 
emp2 = Employee("Rashmi", 200, "softwar")       

print(emp1.departemnt)
print(emp1.esalary, emp1.ename)
emp1.increase()
print(emp1.esalary)
        
