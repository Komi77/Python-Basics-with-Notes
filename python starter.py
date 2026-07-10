print("hello world")

print("---Zaman e fareb mein hatim na ban keh Kumail---\n---Dil shikni he sar e khemam, aabro e naaz nhi---")

# \n is used to leave a line'
print("My favourite word in english is \"Gobbledygook\" ")
#use \" \" to write something in double quote

print("hello", "gobbledygooknihilisticpunk", 27, sep="~", end="loooooooooooooooool")
#use sep="" to seperate words with anything and end="" to write something at the end of a line and becuse of end the next print statement attaches to the one before

print("Cheval") 
print("kinetic energy")

a = 27
print(a)

b = "Kumail"
print("My name is", b, "and the type of b is", type(b)) 

c = True
print(c, "and the type of", type(c))

d = complex(4, 3)
print(d, "The type of d is", type(d))

print(15//6)
#This // divides a number like 15 with 6, but it rounds off the answer to a natural number without decimal

print(9%2)
#This % sign gives us the remainder of this expression after division

print(2**3)
#Means to the power 3

e = 5
f = 3

print("The sum of the two numbers is", e + f)
print("The product of the two numbers is",e * f)
print("The division of the two numbers is", e/f)
print("The rounded off division of the two numbers is", e//f)
print("The remainder after division of the two numbers is",e%f)

g = "2"
h = "3"
print(int(g) + int(h))
# we used int function to convert strings to integers, so that we can get the proper addition result

i = 1.1
j = 8
print(i + j, type(i + j))
# this is implicit typecasting where python will automatically convert the type of j which is an integer to a float(decimal) because it is being added with a float which is i
