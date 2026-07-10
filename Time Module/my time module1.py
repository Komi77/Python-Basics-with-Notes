import time

def usingwhile():
    i = 0 
    while i < 300:
        i = i + 1
        print(i)

def usingfor():
    for i in range(300):
        print(i)


padu = time.time()
#This time.time func gives you time from 1970 in seconds.


usingwhile()
print(time.time() - padu)

usingfor()
print(time.time() - padu)


#we basically ran two similar loops but once with while and second time with for, after running each loop we have written a time.time func, not just that but we have subtracted it from padu which also is a time.time func. what this bascially does is that before any loops are executed, time.time func in padu is executed and it calculated time in seconds, then one loop which in our coding order is the while loop is executed and it runs, then we have executed time.time func (which calcs the time after loop is executed) which is subtracted by time.time func in padu (which calcs time before loop is executed). So, we can find out the time a loop takes to run.


print(4)
time.sleep(3)
print("We are printing this after 3 seconds")

#I think this is pretty self explanatory, the print func is printed after 3 seconds.



t = time.localtime()

tameeztime = time.strftime("%Y-%m-%d %H:%M:%S", t)

print(tameeztime)

#time.localtime gives u your local time, and by using .strftime, we can write it in a very formatted way.
