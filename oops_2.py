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
SM = EMPloyee("SM",200 , "Eng")
NV = EMPloyee("NV", 400 , "Pizza")

print(NV.sal)
print(SM.sal)

SM.change_leaves(55)
print(EMPloyee.leaves)



