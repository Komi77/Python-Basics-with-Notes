class Employee:
    def __init__(self, name):
        self.name = name 
        
    def show(self):
        print(f"The employee name is {self.name}")

class Dancer:
    def __init__(self, dance):
        self.dance = dance 
    def show(self):
        print(f"The dance type is {self.dance}")

class DanceEmployee(Employee, Dancer):
    def __init__(self, name, dance):
        super().__init__(name)
        self.dance = dance 



leo = DanceEmployee("Meetha Khan", "Mujra")
print(leo.name)
print(leo.dance)
leo.show()

#Okay so here we made a class named danceemployee which is made out of two sub-classes(there can be more), now this is multiple inheritance and we can inherit methods used in both classes. Now, pay attention to one thing, in both parent classes there is a func named show, now if i call that in the object leo (which has both classes), which class's func would show? The ans is the class that is written first which in this case is the employee class.

print(DanceEmployee.mro())

#This mro method shows the hierarchy of classes, what i mean is that it shows which class will be considered first. Here, the danceemployee will be seen first amd all its methods, then the employee class, then the dancer class.




