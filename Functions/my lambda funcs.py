def bara(x):
    return x*2


print(bara(5))



dul = lambda x: x*2

print(dul(5))

#So basically lambda functions are just like our regular funcs except you can enclose them inside a variable and write in just one line, they are usually used for simple formulas and expressions like x*2, which is doubling a number, so when you are creating a program where you use these expressions frequently, instead of making a whole ass func, you can make these short and small lambda funcs.

cubing = lambda y: y*y*y

print(f"Holy shite, the cube of 3 is {cubing(3)}")


average = lambda a,b: (a+b)/2

print(average(3,5))


#We can even make a func with 2 values.



semiperimeter = lambda x,y,z : (x+y+z)/2

print(semiperimeter(2,1,4))

#We can even make a func with 3 values.

what = lambda a,b,c,d : (a+c)-(b+d)/a*b*c*d

print(what(6,4,5,8))

#We can even make a func with 4 values.

#You can also make funcs with even more values


def kala(fx, value):
    return 7 + fx(value)


print(kala(cubing, 5))

#How this func works is that we made a func named kala, which inside paranthesis took 2 arguments, one is a func and another is a value, then inside func we wrote fx(value), which means when we are printing kala, we have to first define a func and then a value. This func that we wrote in the argument and in this case is 'cubing', can either be a normal func or a lamba func.

print(kala(lambda x : x*x, 2))

#We can also directly write a lambda func.
