def average (a = 9, b = 6 ):
    averageformula = (a + b)/2
    print("The average of the two numbers is", averageformula)

average()

average(6,7)

c = 3
d =5
average(c, d)



#what we can do is that in the func we can set default values of a and b, so if we just write the func name which in this case is average of 2 numbers, it will take out the avg of the default no. which are 9 and 6. But if we write the func name and define new values of a & b in the paranthesis, it will now take out the avg of the new no. or we could write variable names like c and d and define a numeric value, then write the func name and define the variables in the paranthesis, it will take out the avg of the new no.

average(4)
 
#Another thing that we can do is that we can give the new value of just one variable and the value for the other one will be same as its default value.

average(b = 8)

#This is how to give new value only to the second variable.

average(b = 1, a= 3)

#If we write like this in the pareanthesis where we define variable with their value, then the order does not matter what I mean is that if we put in just the numeric values like (4,5), then python would by default interpret that a = 4 and b =5, but if we write like this in the bracket in which i say b = 1 and a =3, then python would count the first value as value of b and second as value of a.

def name (fname, mname, lname = "Khan"):
    print("Hello", fname, mname, lname)


name ("Peter", "Jofferey")


def avg (*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i

    print("The average of the numbers is", sum/len(numbers))

avg (5, 6, 7, 8, 9)

#for this func what we did is that we put a tupple inside the brackets, how we did it is that we wrote *, then "numbers" which is the container name, so now this container has turned into a tupple, then we used for loop and in the print func we divided sum which automatically adds all the numbers together by len of numbers, which is the length of the tupple named numbers.


def semiperimeter (*nums):
    sun = 0
    for i in nums:
        sun = sun + i

    print("The semi perimeter of the numbers is", sun/3)


semiperimeter(3,4,5)



def avg1 (*numbers):
    slum = 0
    for i in numbers:
        slum = slum + i

    return slum/len(numbers)

q = avg1(5, 6, 7, 8, 9)
print(q)

#what we can do is that instead of writimg print we can use return, then with the use of return we can store the value of the func in a variable lets say q, so what we can do is that we can print q and store its result.
