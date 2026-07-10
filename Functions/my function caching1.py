from functools import lru_cache
import time

@lru_cache
def fx(n):
    time.sleep(5)
    return n*5

print(fx(5))
print("Done for 5")
print(fx(20))
print("Done for 20")
print(fx(6))
print("Done for 6")
print(fx(2))
print("Done for 2")

print(fx(5))
print("Done for 5")
print(fx(20))
print("Done for 20")
print(fx(6))
print("Done for 6")
print(fx(2))
print("Done for 2")

#What this lru cache does is that it stores the cache of the values that we have run for a func like here for these values, for the first time when they run because of time.sleep they have a delay but then you can see that when the values are repeated they are printed instantly, because after running through the values (in one run) it stores its cache and when similar values are again printed they print instantly. 
#NOTE: when the program stops the cache is cleared!

