def cat():
    for i in range(500):
        yield i


far = cat()

print(next(far))
print(next(far))
print(next(far))
print(next(far))
print(next(far))
print(next(far))

#As we print this individually we will start to get our numbers individually.

for j in far:
    print(j)

#This basically runs a loop which iterates every number and runs it.


#Generators are basically like lists, sets etc. but instead of storing the value they more so carry information to create that value when needed. So it saves our memory.

