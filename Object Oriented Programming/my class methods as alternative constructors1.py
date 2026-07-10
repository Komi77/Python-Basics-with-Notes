class Employee():
    def __init__(self, name, salary):
        self.name = name 
        self.salary = salary

    @classmethod
    def fromred (cls, red):
        return cls(red.split("-")[0], red.split("-")[1])
    
    @classmethod
    def fromdog (cls, dog):
        name, salary  = dog.split(",")
        return cls (name,int(salary))



emp1 = Employee("Komi", 12000)
print(emp1.name)
print(emp1.salary)


#This is how we make a class for name and salary of an employee. And we have data in this format.

#But what if i had data in this form salt = "Lewis-5000", now if we wanna print it in the form as it is printed above we can do this;

salt = "Lewis-5000"

emp2 = Employee(salt.split("-")[0], int(salt.split("-")[1]))
print(emp2.name)
print(emp2.salary)

#So, if the data is given in the form of this lewis-5000 means name is lewis and salary is 5000, we can use the split fun and write ("-"), this - means that a list will be created b/w the string, and the - will considered as the divider.

#But this code doesnt look so good here it is very complicated and looks bad, so we can put this whole split("-") code inside the class and to learn how to do this, lets make one more variable;

red = "Phil-7500"

emp3 = Employee.fromred(red)
print(emp3.name)
print(emp3.salary)


#Here you can see we had the data in a very unorganized form (info was separated with a dash -), but instead of making it accessible to print in an organized manner here, we do that inside the class with the help of class methods, you can see how we do that above inside the class, but this is how we mainly use class methods as alternate constructors.

#in another example we have a string dog;

dog = "Tommy,3900"

emp4 = Employee.fromdog(dog)
print(emp4.name)
print(emp4.salary)