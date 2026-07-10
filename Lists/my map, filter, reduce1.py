def cube(x):
    return x*x*x


lip = [2,4,5,6,7,9]


cherry = list(map(cube, lip))

print(cherry)


#What we did is that we had a func named cube pretty self explanatory, then we had a list named lip, which had some numbers, now we want a list that is filled with the cube of every number in the lip list, so how do we do that, voilla introducing the map func, just write the func name and the list name inside the paranthesis and the badboy will apply the func to every item in the list.
#But we have to write list, before map to get a fucking list.


def shaboom(a):
    return a > 4


jer = list(filter(shaboom, lip))

print(jer)

#What the filter func does is that it takes specific instructions from the func given and then applies it to the list given, then the new list (For which we have to write 'list' before filter), now this func says that only take numbers greater than 4, and we applied this to the list lip and made a new list that fulfills the filtering demand. 


umami = list(map(lambda x : x*x, lip))

print(umami)

#We can also use a lambda func in the perenthesis. 


from functools import reduce

zam = [1, 2, 3, 4, 5]

def lol(x, y):
    return x + y

pro = (reduce(lol, zam))

print(pro)


#The reduce func basically reduces a list to just one item, now it depends on your func in the paranthesis how its gonna do so, in this func for e.g. lol, it adds every first and second item in the list, so 1 and 2 become 3, 3 and 3 become 6, 6 and 4 become 10 and 10 and 5 become 15. Thats the output.


def patrol(x,y):
    return x*y

goo = reduce(patrol, zam)

print(goo)

#another e.g. of reduce with some other func argument.
