class Daddy():
    def abbu(self):
        print("Hey i am your abbu")

    
class Son(Daddy):
    def beta(self):
        print("Hey i am your beta")

        super().abbu()

a = Son()
a.abbu()
a.beta()


#now we know that the class son comes from the class daddy, but how can i call funcs from daddy to son, for that we can just use the super keyword and then write the name of the func, or any variable we wanna call like we did here for a func named abbu, but NOTE: if there was a function named beta inside son already then we call it, it will call that func, but if we want it to not call this func rather the func with the same name but from the daddy class, for that we use super keyword.



#ANOTHER EXAMPLE:

class Cop():
    def __init__(self, name, id):
        self.name = name
        self.id = id


class Captain(Cop):
    def __init__(self, name, id, meetings):
        super().__init__(name, id)

        self.meetings = meetings


b = Captain("Raymond Holt", 99, 32)
print(b.id)

        