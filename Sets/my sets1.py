a = {2,4,2,6}
print(a)

#Set doesn't repeat values like 2 will only come once.
#Sets are immutable 
#Set is also disordered, means if we write 2,4,2,6 , it can print the result as 4,2,6 (2 will be only printed once), so that is why it is disordered, and that is also why we cant change items at certain indexes for e.g. if there is 2 at index 0, I cant change it because they are disordered.

info = {"Carla", 24, "Los Angeles", True, 92.34}
print(info)

for items in info:
    print(items)



#To make an Empty set:

c = {}
print(type(c))

#This is a wrong way to make an empty set, this will make an empty dictionary.

#Correct Way:

d = set()
print(d, type(d))