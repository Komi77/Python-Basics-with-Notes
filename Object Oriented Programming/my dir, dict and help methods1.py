x = [1,2,3]
print(dir(x))

#What the dir method does is that it shows us all the methods that we can do in a list like reverse, extend, count, all of them. So, we can know if we can use a specific method or not, like if we want to see if we can do the .add method or not, we can simply just print it here, if it throws an error then we cant do it but if doesnt then it is a method.
print(x.__add__)


class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.human = True

    def pagal(self):
        self.pagal = False

p = Person("Jhonny", 23)
p.pagal()
print(p.__dict__)


#dict is used to see what is written inside a class, especially what is written inside a self func, and it prints it in the form of a dictionary.

print(help(str))

print(help(Person))

#The help method helps us to know all about a class, like a string denoted by str is also a class, so we can use 'help' to know more about it, similarly we made a class named Person, and we can get info bout it using help.





    