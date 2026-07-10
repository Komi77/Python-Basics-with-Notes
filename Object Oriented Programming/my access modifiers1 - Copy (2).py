#Public Modifier:

class Employee:
    def __init__(self):
        self.name = "Kumail"

    
nigga = Employee()
print(nigga.name)


#This is a public modifier what it means is that we can access it outside of the class, means that if there is a variable named name inside a class called Employee then we assign a variable nigga for the class employee then when we try to print a variable that was inside the class from the outside, it works so this is known as a public modifier.


#Private Access Modifier:

class Fuk:
    def __init__(self):
        self.__duck = "battakh"


hag = Fuk()
'''print(hag.__duck)'''
print(hag._Fuk__duck)

#Now this is a private modifier, what happens is that if we write a variable inside the class with two underscores before it, it will make a private modifier. NOTE: These things like public, private, protected modifiers donot naturally exist in python but we make them ourselves. So by doing this we make a private modifier. And as you can see that when we tried to use/print it outside the class, we couldn't. But there is a way to do it and for that we also have to mention the the class name and before that we have to put an underscore. That is how we indirectly access Private Modifiers.


class Student:
    def __init__(self):
        self._marks = 84


class Subject(Student):
   pass

yem = Subject()
print(yem._marks)

#Focus on the variable that we make inside the class student named ._marks now that single underscore holds great significance because it indicates that the variable that we just created with a single underscore before it should only be used by another class and should not be accessed outside any class, like the ._marks variable is transfered to the class subject after inheritence, so we use this convention to highlight and basically tell ourselves that we should not use it outside classes, but we can. As you see we printed yem._marks and it printed so we can print these or use them outside classes however we shouldn't and the underscore is a general highlighter which tells the programmer to not to such thing. We can also use other symbols lets say for e.g. $ or # etc. for this purpose too.

