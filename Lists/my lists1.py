a = [3, 6, 7]
print(a)
print(type(a))

marks = [5, 8, 2]
print(marks[0])
print(marks[1])
print(marks[2])

#Lists are mutable (can be changed)

b = [3, "Komi", 7, True]
print(b[-3])

if ("Raza" in b):
    print("Yes")

else:
    print("Fuck nah")

if ("Komi" in b):
    print("Yes")

else:
    print("Fuck nah")

if ("omi" in "Komi"):
    print("Fuck yeah", b[1])

else:
    print("Aw Hell nah")


d = [3, 6, 4, "Gobbledygook", True]
print(d[2:-1])


e = [3, 5, "Hi", 2, 1, 0, False, "Flip", 7, 8, 12, 24, 34, 67, 98]
print(e[:])
print(e[1:len(e)-2])
print(e[1:len(e)-2: 3])
#This new 3 after colon is how many indexes will get skipped over, if its 3 written here it means that it skips 3 numbers, so if its initial splice value is 1, then it skips 3 and starts from 5, then it skips 5, "Hi" and 2 and 1 will be printed. So, in skipping like this whenever the index is on a number and certain indexes have to be skipped like here 3 have to then it would skip itself, then the next, then the next.

f = [i for i in range(10)]
print(f)
#This will generate a list from nunmbers 0 to 9, so for eg if we want to generate a list of numbers, we dont have to write them again and again.
#NOTE: it is known as list comprehension

g = [i*i for i in range(10)]

h = [i+1 for i in range(10)]
print(h)

j = [i*i for i in range(10) if i%3==0]
print(j)
#While generating a list by using for loop, we can also give if instructions!
