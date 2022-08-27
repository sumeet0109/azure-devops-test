class EMPloyee:
    leaves = 8
    def __init__(self, aname, asal ,arole):
        self.name = aname
        self.sal = asal
        self.role = arole
        
    def printdetails(self):
        return f"name is {self.name}. sal is {self.sal} & role is {self.role}"

    @classmethod
    def change_leaves(cls,newleaves):
        cls.leaves = newleaves

    @staticmethod
    def printgood(string):
        print("This is good" + string)

SM = EMPloyee("SM",200 , "Eng")
NV = EMPloyee("NV", 400 , "Pizza")

class Coder(EMPloyee):
    def __init__(self, aname, asal ,arole ,alanguage):
        self.name = aname
        self.sal = asal
        self.role = arole
        self.language = alanguage
    def printprog(self):
        return f"Coder name is {self.name}. sal is {self.sal} & role is {self.role} also languages known are {self.language}"

aa = Coder("aa", 555 , "coder" ,["python", "c++"])
nn = Coder("nn" , 777 , "coder", ["java", "node"])
print(aa.printprog())
print(nn.language)




