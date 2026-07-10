#Multilevel inheritance simply means, there is a parent class, then from that class one child class is made and from that child class another child class is made.
#Understand it by this analogy, Grandfather --> Father --> Son.

class Human:
    def __init__(self, color):
        self.color = color

    def show(self):
        return print(f"The color of the human is {self.color}")
    

class Employee(Human):
    def __init__(self, color, name):
        super().__init__(color)
        self.name = name

    def show(self):
        Human.show(self)
        return print(f"The color of the human is {self.name}")    

class Programmer(Employee):
    def __init__(self, color, name, codinglanguage):
        super().__init__(color, name)
        self.codinglanguage = codinglanguage

    def show(self):
        Employee.show(self)
        return print(f"The color of the human is {self.codinglanguage}")    
    


paad = Programmer("White", "Shakespare", "C++")
print(paad.color) 
print(paad.name)
print(paad.codinglanguage)
paad.show()


#This is multilevel inheritance as you see, now for the func show, what happens here is that in the show func of the class employee i also wrote the show method of human, similarly in the show func of class programmer, i wrote also wrote the show method of employee, so now when i run the show method of programmer, these show method of all the three classes will run in chronological order.
