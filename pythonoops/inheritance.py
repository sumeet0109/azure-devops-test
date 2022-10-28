
class Employee:

    increment = 1.5
    def __init__(self, name, salary, dept):
        self.ename = name
        self.esalary = salary
        self.departemnt = dept

    def all_details(self):
            print("all employee ",  self.ename,  self.esalary, self.departemnt)      

    def increase(self):
        self.esalary = int(self.esalary * self.increment )    

class Programmer (Employee):
    def __init__(self, name, salary, dept, programming_language, experience):
        super().__init__(name, salary, dept)
        self.programming_language = programming_language
        self.experience = experience

emp1 = Employee("sumeet", 100, "IT") 
emp2 = Employee("Rashmi", 200, "softwar")    
emp1.all_details()
emp2.all_details()

# print(emp1.departemnt)
# print(emp1.esalary, emp1.ename)
# emp1.increase()
# print(emp1.esalary)


emp3 = Programmer("pritika", 500, "Developer", "nodejs", "1 yrs")



print(emp3.programming_language)


        
