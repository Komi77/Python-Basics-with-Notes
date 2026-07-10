def factorial(n):
    if (n == 0 or n == 1):
        return 1
    
    else:
        return n * factorial(n-1)
    

#Recursion is when you call the function itself within itself. What i mean is that in the else portion, to find the factorial of numbers, I say multiply n by factorial (n-1) which means i am calling the function factorial(n) but i have changed the situation just a bit from factorial(n) to factorial(n-1). That is called recursion. How this function works is that we say that multiply n which is for e.g 5 with factorial(n-1) means 4!, then it keeps on reducing to 5 *4*3*2*1!, now python sees that 1! or factorial 1 has the value of 1, so it stops and gives the ans.

print(factorial(5))
print(factorial(6))
print(factorial(3))




#Fibonacci Sequence:
#f(0) = 0
#f(1) = 1
# f(2) = f(1) + f(0)
# f(3) = f(2) + f(1)
# f(n) = f(n-1) + f(n-2)

def f(e):
    if(e == 0):
        return 0 
    
    elif(e == 1):
        return 1
    
    else:
        return f(e-1) + f(e-2)
    

print(f(5))
    
