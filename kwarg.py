### Keyword variable Lenght Arguments ###

def person(name, **data):
    print(name)
    print(data)

person("sumit", age= 41, mobile = 123456789 , city ="kyn" )

### Also same can be done via for loop ###

def person(name, **data):
    print(name)
    for i , j in data.items():
        print(i,j)


person("sumit", age= 41, mobile = 123456789 , city ="kyn" )
