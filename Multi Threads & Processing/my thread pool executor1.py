import time
import threading
from concurrent.futures import ThreadPoolExecutor


def func(seconds):
    print(f"The time taken is {seconds} seconds")
    time.sleep(seconds)


'''

def pool():
    with ThreadPoolExecutor() as executor:
        future1 = executor.submit(func, 3)
        future2 = executor.submit(func, 2)
        future3 = executor.submit(func, 4)

        print(future1.result())
        print(future2.result())
        print(future3.result())

pool()

'''

#So basically threadpoolexecutor is used to schedule the execution of funcs, here you can see that first it will run all the funcs but then it will print the results together, which means it schedules them so that they can be printed at once.


def paad():
    with ThreadPoolExecutor() as executor:
        l = [3, 5, 6, 8]

        results = executor.map(func, l)

        for result in results:
            print(result)

paad()

#here if we have some values in a list and we want to put them in a func and run it all of them at once simultaneously then, we can use the threadpoolexecutor's map method.
