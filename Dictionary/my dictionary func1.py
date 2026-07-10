ep1 = {122: 45, 123: 73, 124: 98, 125: 54}
ep2 = {231: 76, 268: 67}
ep1.update(ep2)
print(ep1)
#Updates the dictionary ep1 by adding ep2 at the end.


ep3 = {122: 45, 123: 73, 124: 98, 125: 54}
ep3.clear()
print(ep3)


ep4 = {122: 45, 123: 73, 124: 98, 125: 54}
ep4.pop(123)
print(ep4)
#Write any key inside the brackets and that key and value will be deleted


ep5 = {122: 45, 123: 73, 124: 98, 125: 54}
ep5.popitem()
print(ep5)

#Removes the last key & value


ep6 = {122: 45, 123: 73, 124: 98, 125: 54}
del ep6[125]
#Deletes a specific key and value.
print(ep6)


about = ("name", "place", "animal")
who = ("Komi", "Gujar Nala", "Octupussy")
ep7 = dict(zip(about, who))
print(ep7)
#This is how to make a dictionary from lists


lol = ("name", "place", "animal")
why = "none"

ep8 = dict.fromkeys(lol, why)
print(ep8)
#We use .fromkeys when we want to make a dict from lists but we want the same value for every key which in this case is "none".





