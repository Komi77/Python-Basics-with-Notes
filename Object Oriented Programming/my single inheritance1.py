class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def Makesound(self):
        return print("The animal makes sound")
        
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species = "Dog")
        self.breed = breed

    def Makesound(self):
        return print("The dog Barks!!!")
    
oui = Animal("Teddy", "Goat")
print(oui.Makesound())

red = Dog("Paddu", "Husky")
print(red.Makesound())

#This just simply shows how we inherited a class Dog from another class Animal so this is simply single inheritance, moreover, we also overwrote the function makesound.


class Cat(Animal):
    def __init__(self, name, colour):
        super().__init__(name, species = "Cat")
        self.colour = colour


    def Makesound(self):
        return "Cat says MEOWWWWW"
    

ev = Cat("Terminatorpulsatdestroyer73", "black like a nigger") 
print(ev.Makesound())
print(ev.colour)