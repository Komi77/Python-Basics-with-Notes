a = [45, 6, 78, 1, 4, 3]
print(a)
a.append(7)
a.append("Nigga")
print(a)
#Adds anything at the end of the list

b = [45, 6, 78, 1, 4, 3]
b.sort()
#sorts a list in ascending order
print(b)

c = [45, 6, 78, 1, 4, 3]
c.sort(reverse=True)
print(c)
#Now it sorts in descending order

d = [45, 6, 78, 1, 4, 3]
d.reverse()
print(d)
#It just reverses the whole list

e = [45, 1, 6, 1, 78, 1, 4, 3, 1]
print(e)
print(e.index(1))
#In this func we can write any value whether it be a integer or a string and it will give its index number where it occured the first time. Means that in this list 1 appears many times but this func will only give the index of 1 where it appeared first.
#NOTE: We have to use the .index() func in print statement. 



f = e.copy()
print(f)
print(f.count(1))
#Here we used two functions, one is the copy function where I said that i am making a new list f which is the exact copy of a previous list named e, so instead of manually copying the matter of e into f, I can just use this func.
#Second is the count function, its pretty straightforward, it counts how many times a certain integer or anything comes in a list.
#NOTE: We have to use the .count() func in print statement. 
        

g = f.copy()
g.insert(1, 899)
g.insert(4, "LOL")
print(g)
#By using the .insert() func we can insert any thing inside our list at any desired index, first write the index, then the integer of string or whatever


list1 = ["crab", "dragon", 4, False, 3, 1]
list2 = ["dog", 3, 4, 'fog']
list1.extend(list2)
print(list1)
print(list2)

#What we did here is that we added list 2 at the end of list 1 by using the .extend() method. Means we extended list2 and appended it at the end of list 1.


m = list1.copy()
l = list2.copy()
k = l + m 
print(k)

#Another way to add to lists is that we can directly use the addition sign, but the catch here is that this creates a new list which in this case is k whereas when we used the extend func, it added the second list (the list that we said to extend) into the first list and it didnt creat a new list

lsd = [3, 4, 5, 17]
lsd[0] = 90
print(lsd)
#we can change any number object at a specific index.

fls = [3, 4, 5, 17]
fls.pop(3)
print(fls)
#Remove item from the specific index like index 3 in this case.
