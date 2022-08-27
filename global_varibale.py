
a = 12 ### GLobal Varibale

def something():
    a = 12 ### variable a is again called but definition scope not in global scope
    print( "in func", a) 

something()

print("global", a)

### To chnage the GLobal varibale under the definition scope

a = 12 ### GLobal Varibale

def something():
    
    global a ### if we need to change the GLobal varible under definition scope use global keyword
    a = 20
    print( "in func", a)

something()

print("global", a)



### if we want 'a' varibale in 'global & 'Local" scope the above script will not work need to add 'Globals" keyword
a = 12 ### GLobal Varibale

def something():
    a = 9
    x = globals() ['a']
    print( "in func", a)
    globals() ['a'] = 15
something()

print("global", a)

