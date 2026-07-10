#'==' basically just identifies if two values are the exact same or not, like "pizza" and "pizza" are same but, 4 and "4" are not same. 

#On the other hand, 'is' tells us if two certain things are the same thing. Now let that sink in because for e.g. if i make a list lets say a which consists of numbers and then create list b which is exactly the same, if we write a is b, it will be false. Because list are mutable means they can be changed, so in pythons little mind when we create list a then the list b is exactly same as a, python doesnt see list b as the copy of a, it sees it as a whole new being (although clearly its the same) but python doesnt see it that way and there is a good reason because lists can be changed, and for e.g. if sometime in the future a or b gets changed then they will not be the same, so they are not the same thing even if they seem alike. Now in the case of single values or tuples if they are the same then we can say that tupple a is tupple b, because python knows that tupples cant be changed or values cant be changed, so if we write that exact tupple again or value again, python will recognize it as the same thing from the same location in its memory database, so for python it is the same thing.

a = [1,2,3]
b = [1,2,3]

print(a == b)
print(a is b)

c = (1,2,3)
d = (1,2,3)


print(c == d)
print(c is d)

e = "komi"
f = "komi"

print(e == f)
print(e is f)

g = None
h = None

print(g == h)
print(g is h)


