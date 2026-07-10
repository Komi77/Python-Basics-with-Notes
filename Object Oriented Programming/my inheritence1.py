class Cop:
    def __init__(self, name, id, arrest):
        self.name = name
        self.id = id
        self.arrest = arrest

    def show(self):
        print(f"The name of the employee: {self.id} is {self.name } and he made {self.arrest} arrests this year")

copper = Cop("Jari", 567, 42)
print(copper.name)        
print(copper.id)        
print(copper.arrest)
copper.show()

#What we did is that we made a sort of info class for a cop he is just a regular cop, but what if i say that i want to make a similar class for a sergent, the big problem is that sergent has more duties, so we'll need to add more info, so how can i make a new class for him, which would include all these details and some more, well we can use the inheritence property for that. Here is how it works:

class Sergent(Cop):
    def __init__(self, name, id, arrest, meetings, hires, fires):
        super().__init__(name, id, arrest)

        #This super().blah blah blah brings back the arguments from the parent class.

        self.meetings = meetings
        self.hires = hires
        self.fires = fires

    def crow(self):
        print(f"The employee attended {self.meetings} meetings, and he hired {self.hires} people, and he fired {self.fires} people")


jeff = Sergent("Jeffords", 321, 67, 21, 9, 2)
print(jeff.name)        
print(jeff.id)        
print(jeff.arrest)
print(jeff.meetings)
print(jeff.hires)
print(jeff.fires)
jeff.show()
jeff.crow()


#As you can see we have successfully inherited one class to another!