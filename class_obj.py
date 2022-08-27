class EMPloyee:
    leaves = 8
    def printdetails(self):
        return f"name is {self.name}. sal is {self.sal} & role is {self.role}"
SM = EMPloyee()
NV = EMPloyee()

SM.name = "SM"
SM.sal = 200
SM.role = "Eng"

NV.name = "NV"
NV.sal = 300
NV.role = "pizza"
print(NV.sal)
print(EMPloyee.leaves)
EMPloyee.leaves = 10
print(EMPloyee.leaves)
print(SM.printdetails())





