#Local variables are the varibles that are made inside a func and you can not use them outside the func or without executing the func. Global variables however are made the ones made outside a func and they can even be used inside a func if there aint a variable inside the func having the same name.


x = 4 
print(x)

def yello():
    x = 5
    '''
    this x whos value is 4, is a local variable, however the x outside is global variable. So if we call x outside the func, its value will be 4 not 5.
    '''
    print(f"the local variable is {x}")
    print("Wassup homes")



yello()
print(f"the global variable is {x}")



hodor = "Fucking nigger"

def lolzzz():
    print("Puta")
    print(hodor)


#Now in this func as you see we are printing a global variable which means that ift isnt inside the func rather outside but still we can print it. NOTE: IF another variable named hodor is made inside the func, then fun would print the matter inside that hodor variable rather than printing the global one.

lolzzz()



a = 10

def gerr():
    global a 
    a = "pajeets"
    print(a)
    print("Will this work")


gerr()
print(a)

#Not only can we use a global variable inside a func, moreover we can even change its value while remaining inside the func by using the global keyword, now what we did is that we had the value of a as 10, inside the func we used global keyword and changed it to 'pajeets', and when i printed the value of a outside the func now, it actually changed to 'pajeets'.