class A:
    classvar1 = ' i m a class variable in class A'
    def __init__(self):
        self.var1 = ' i am inside class A constructor'
        self.classvar1 = 'i am instance variable class A'

class B (A):
    classvar2 = ' i am in class B'
    def __init__(self):
        self.var1 = ' i am inside class B constructor'
        self.classvar1 = 'i am instance variable in class B'
        super().__init__()
        print(super().classvar1)

a = A()
b= B()
print(a.classvar1)    



