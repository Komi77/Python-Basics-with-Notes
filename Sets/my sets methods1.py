s1 = {4, 5, 7}
s2 = {3, 5, 1}
print(s1.union(s2))
#This union of the two sets creates a new set, the o.g. sets are not changed.

a = {4, 5, 7}
b = {3, 5, 1}
a.update(b)
print(a)
print(a, b)
#Now what we have done is that we changed the set 'a', such that now it also contains the values of b.

cities1 = {"Tbilisi", "Ulanbataar", "Bandar Seri Begawan", "Islamadbad"}
cities2 = {"Dili", "Nypyidaw", "Astana", "Tbilisi"}

cities3 = cities1.intersection(cities2)
print(cities3)

#Again in the intersection of the two sets, we are not changing them, instead we are creating a new set.

c1 = {"Tbilisi", "Ulanbataar", "Bandar Seri Begawan", "Islamadbad"}
c2 = {"Dili", "Nypyidaw", "Astana", "Tbilisi"}

c1.intersection_update(c2)
print(c1)

#what we did here is that we changed the set c1, and now it will only contain the values of the intersection b/w its values and c2 set's values.

d1 = {"Tbilisi", "Ulanbataar", "Bandar Seri Begawan", "Islamadbad"}
d2 = {"Dili", "Nypyidaw", "Astana", "Tbilisi"}
d3 = d1.symmetric_difference(d2)
print(d3) 

#what it actually does is;
#(A U B) - (A ∩ B)

e1 = {"Tbilisi", "Ulanbataar", "Bandar Seri Begawan", "Islamadbad"}
e2 = {"Dili", "Nypyidaw", "Astana", "Tbilisi"}
e3 = e1.difference(e2)
print(e3)

#It is the basic A-B in maths, where we are creating  a new set e3 which will contain all the items of the first set (e1) except the items that are common.


f1 = {"Tbilisi", "Ulanbataar", "Bandar Seri Begawan", "Islamadbad"}
f2 = {"Dili", "Nypyidaw", "Astana", "Tbilisi"}
f3 = f1.isdisjoint(f2)

print(f3)
#Simply identifies if the two sets are disjoint or not.


fer1 = {2,4,6,8}
fer2 = {2,3,5,7}

print(fer1.issuperset(fer2))

wq1 = {"Ronaldo", "Messi", "Neymar", "Modric"}
wq2 = {"Ronaldo", "Modric"}

wq3 = wq1.issuperset(wq2)
print(wq3)

wq4 = wq2.issubset(wq1)
print(wq4)


zeb = {"Lion", "Tiger", "Cheetah"}
zeb.add("Shepard")
print(zeb)

#By using .add we can add a single item into a set, however we use .update if we want to add another set into it.


play = {"Lion", "Tiger", "Cheetah"}
play.remove("Lion")
# play.remove("Panther")
print(play)
 

far = {"Lion", "Tiger", "Cheetah"}
far.discard("Panther")
print(far)

#Remove and discard both do the same function, the only diff is that when we use .remove and try to remove something that isnt there, it throws an error, however if we do the same with    .discard, it doesnt throw any error.


cs = {"Lion", "Tiger", "Cheetah"}
cs.pop()
print(cs)
#This will randomly pop out or remove any item from the set


verb = {"Lion", "Tiger", "Cheetah"}
del verb

#del isnt a function, rather it is a keyword which deletes the whole set.

crab = {"Lion", "Tiger", "Cheetah"}
crab.clear()
print(crab)

#When we dont want to delete the entire set, but just wanna delete its value we use .clear() .






