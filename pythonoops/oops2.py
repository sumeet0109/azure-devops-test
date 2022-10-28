class Computer:
    def __init__(self, cpu, ram):
        self.cpu1 = cpu
        self.ram1 = ram
    def config(self):
        print("Config is ",  self.cpu1,  self.ram1)
         
com1 = Computer("i5", 16)
com2 = Computer ("Ryzen 3", 8)        

com1.config()
com2.config()
print(com1.ram1)
       
