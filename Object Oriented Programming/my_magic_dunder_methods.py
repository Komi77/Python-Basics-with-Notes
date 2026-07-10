#Dunder methods are all the methods that start and end with __ like __init__ or __len__, but when we have to call them we dont do it by writing __, in some methods we literally dont have to call them like the init method but when we call len method we dont write the double underscore we just call it by its name like;

class Employee:
    name = "Kumail"
    def __len__(self):
        return len(self.name)
    

    def __str__(self):
        return f"The name of the employee is {self.name}"

    def __repr__(self):
        return f"Employee ganja is {self.name}"

#NOTE: To see how these two methods work method works, coordinate with the file named sample.py

    def __call__(self):
        return print("You are in the class Employee")
        



a = Employee()
print(a.name)
print(len(a.name))

#So to get the length of anything in a class we use this dunder method __len__.


a()
#this is the call method, we can use it by just writing the variable name and then brackets, there can be many use cases for it, i think this use case which tells the user which class he is in is a very good use case for this method.