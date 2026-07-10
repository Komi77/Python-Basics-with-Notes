dic = {
    "Name": "Kumail",
    "Place": "Yerevan",
    "Animal": "Yeti",
    "Thing": "Belt"
}
print(dic)
print(dic["Name"])

#Dictionaries are ordered set of values.
#Anything before semi colon is know as the key. And anything after it is the value, if we want to print the value, we have to mention the key in print.

candidate = {
    22081: "Kumail",
    12322: "Jari",
    24321: "Rooney",
    32143: "Jacob"
}
print(candidate[12322])




yer = {
    "Name": "Kumail",
    "Place": "Yerevan",
    "Animal": "Yeti",
    "Thing": "Belt"
}
# print(dic["Name2"])
print(yer.get("name2"))

#Both do have the same func, but if i ask for a key that doesnt exist in the dictionary, the first method will throw an error, however the second method in which we use .get(), just says none. 

print(yer.keys())
#This is how you can print all and only the keys.

print(yer.values())
#This is how you can print all and only the values.



sel = {
    "Name": "Kumail",
    "Place": "Yerevan",
    "Animal": "Yeti",
    "Thing": "Belt"
}

for allkeys in sel.keys():
    print(allkeys)

#This will give the keys individually.

for allvalues in sel.values():
    print(allvalues)
#This will give the values individually.






call  = {
    "Name": "Kumail",
    "Place": "Yerevan",
    "Animal": "Yeti",
    "Thing": "Belt"
}



for wowkeys in call.keys():
    print(f"The value correcponding to the key {wowkeys} is {call[wowkeys]}")


#This is how we can individually print keys and values and also write them in a sentence, we used f string for it, then we wrote {wowkeys}, which is the iterated or the individual key items, then we wrote {call[wowkeys]}, call is ofcourse a variable, and wowkeys is the iterated or individual key items, but if we write them both together inside an f string in this manner, it will actuallly print the value. So thats how we did it.



free  = {
    "Name": "Kumail",
    "Place": "Yerevan",
    "Animal": "Yeti",
    "Thing": "Belt"
}

for wowvalues in free.values():
    print(wowvalues)


for wowkeys in free.keys():
    print(f"The value correcponding to the key {wowkeys} is {wowvalues}")

#Another method!


mrp  = {
    "Name": "Kumail",
    "Place": "Yerevan",
    "Animal": "Yeti",
    "Thing": "Belt"
}

print(mrp.items())

#Print every key with its value in a pair

for key, value in mrp.items():
   print(f"The value correcponding to the key {key} is {value}")
    



