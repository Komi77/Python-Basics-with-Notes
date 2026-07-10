a = (5, 6)
print(type(a), a)
#Tupples are immutable (can't be changed)


b = (1,)
print(b)
#If we want to make a tupple with just one element then we have to put a comma after it, else it will not be registered as a tupple instead it will be registered as a string.


c = (56, 78, "hi", True, 544, 69, 0.007)
if(0.007 in c):
    print("Oh yeah")
else:
    print("Fuck off cunt")


d1 = (56, 78, "hi", True, 544, 69, 0.007)
d2 = d1[1:4]

print(d2)
#we can also splice tupples but we dont change the og tupple instead create a new one.

e = (56, 78, "hi", True, 544, 69, 0.007)
print(e[0])
print(e[1])
print(e[2])
print(e[3])
print(e[4])