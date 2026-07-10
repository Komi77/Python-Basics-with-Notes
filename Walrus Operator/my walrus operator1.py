#walrus operator basically overwrites a program and it is also used to write a program shortly.

a = True
print(a:= False)

#This sort of overwrites a and returns a false value.

daku = []

while True:
    lol = input("Whats your fav food?: ")
    if lol == "quit":
        break
    daku.append(lol) 
print(daku)

#we wrote this code simply using while loop, now we will write it using the walrus operator, and you'll see how short it makes the code.

paani = []

while (jat:= input("Input your fav drinks: ")) != "quit":
    paani.append(jat)

print(paani)


#Here as you see we used the walrus operator and the code that we previously wrote in so many lines is now writing in only few.
