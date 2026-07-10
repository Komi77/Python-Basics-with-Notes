import threading
import time

def func(seconds):
    print(f"The time taken is {seconds} seconds")
    time.sleep(seconds)

# func(4)
# func(2)
# func(1)

#Here if we try to execute the function like this you will see that first the first func executes then the second, then the third. So, it will take alot of time. Think of it as downloading something of the internet, if we have to download 3 things why should we first download one, wait for it to be downloaded then download the second and then third. Thats why we use threading.

time1 = time.perf_counter()

t1 = threading.Thread(target= func, args= [4])
t2 = threading.Thread(target= func, args= [2])
t3 = threading.Thread(target= func, args= [1])

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

time2 = time.perf_counter()

print(time2 - time1)

#here by using threads what we basically did is consider it like this, we had to download 3 things from the internet, so as i said earlier we dont have to first download one thing and wait for it to be finished then download the second and then third, what we can do is that we can start downloading all 3 things at once. However, this doesnt mean that the first thing will be fully downloaded or understand it like this if we take the diff of time performance, we will see that its even less than 1 sec because here we are just saying to download the things at once, we dont care of when it will get fully downloaded, that is why the time performance diff will also give the time in which all 3 things were started to download, if we want the time perf diff of when all these things are downloaded then we can use the join method for, then the time perf diff will give the time for when all 3 things were started being downloaded at once and then when were they fully downloaded.
