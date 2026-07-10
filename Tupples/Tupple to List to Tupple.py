#METHOD 1:
#If we want to add something to a tupple, we can't directly, so we first convert the tupple into a list, add those things, then convert that list again to a tupple.

cars = ["Ferrari", "Mclearn", "Lambo", "Nissan"]
goated = list(cars)
goated.append("Shevy")
goated.append("Mehran")
goated.remove("Nissan")

cars = tuple(goated)
print(cars)


#METHOD 2:
countries1 = ("Pakistan", "India", "East Timor")
countries2 = ("USA", "UK", "Indonesia")

countriesTogether = countries1 + countries2

print(countriesTogether)

#One more method is that we can make two tupples, then create a new tupple which is a combination of the previous two.

a = (34, 56, 6, 7, 3, 2, 5, 3, 21, 90, 3, 54, 3)
res =a.index(3, 4, 8)
print(res)
#So we created a new tupple which calculates the index of a specific item, the first time it occurs (which is 3 in this case), but the interesting thing that we did here is that we also gave splicing instructions, so now python will look when did 3 occur for the first time from the index 4 to index 7.

