#CREATING A CLASS:
class Person:
    name = "Kumail"
    occupation = "Astronomer"
    def lol(self):
        return print(f"{self.name} is a {self.occupation}")



#CREATING OBJECT#1:
a = Person()
a.name = "Turab"
a.occupation = "Darzi"
print(a.name)
print(a.occupation)
a.lol()


#This is how we first learned to create classes, but what if i tell you that there is an easy way to do it, yes i told you that by using classes we dont have to write those pre-printed headings like "name" or "occupation" headings again and again, but we kinda are when we are creating an object a. 
#So a more convinient method to do it is known as constructors;
#And they work like this;

class Person1():
    def __init__(self, name, occupation, huzz):
        print("Hey i am an alien")
        self.name = name 
        self.occ = occupation 
        self.huzz = huzz

    def info(self):
        print(f"{self.name} is a {self.occ} and he has {self.huzz}")


e = Person1("Kumail", "Footballer", None)
print(e.name)
print(e.occ) 
print(e.huzz) 

e.info()

#As you see we dont have to write a.name = blah blah and a.occupation = bfsdgd again and again, we can just firstly make this function in the class, where we can define these so called pre printed headings, then when we are creating an object we can write the answers (inputs) to these headings in the paranthesis, no need to write these big blocks of text.