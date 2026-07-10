from my_magic_dunder_methods import Employee

e = Employee()
print(e)
print(str(e))
print(repr(e))

#Here we have imported a class from our other file, now if i make an object e from this class and if i want to print e, i will get some wierd gobbledygook printed, means the content of the class employee wont be printed, so for that in our main file, i can make a __str__ method and put things inside that, so that when i print e now i will see that it will print the content which is inside the str method.

#We also made a repr method but you can see that when we print e, str will be printed and repr wont, so when we print the object like e, str will always be the first priority to be printed, repr will only be printed if str isnt there, we can also print them directly.

e()