a = 8
b = 6

geomean1 = (a*b)/(a+b)
print(geomean1)

c = 10
d = 5

geomean2 = (c*d)/(c+d)
print(geomean2)

#we have written a code to find out the geometric means of two numbers a and b, then c and d. notice how we use the same code or formula for both of them but to make it easy and not write this code again and again we can use a function.

def geometericmean (a,b):
    mean = (a*b)/(a+b)
    print(mean)

#now we have created a function and we can just write its name beneath two numbers and their geo mean will be calculated.

e = 8
f = 6
geometericmean (e, f)

g = 10
h = 5
geometericmean (g, h) 


def whoisgreater (i, j):
    if(i>j):
        print("The first number is greater")

    elif(i == j):
        print("Both the numbers are equal")

    else:
        print("The second number is greater")


i = 5
j = 5
whoisgreater (i, j)

k = 7
l = 10
whoisgreater (k, l)


def whoislesser (a, b):
    pass

#we defined a func named whoislesser, lets assume this func is to identify which number is smaller, but the thing is that I dont wanna write the body of this func rn, instead maybe I'll write it after sometime but I have defined it so that I dont forget that I want to write a func like this, so what i can do is that for now i can just write pass beneath the func and python wont throw any error and i can move on.
