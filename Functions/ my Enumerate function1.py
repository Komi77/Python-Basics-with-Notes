marks = [45, 74, 21, 38, 98, 23, 12]

for index, mark in enumerate(marks):
    print(index, mark)
    if (index == 4):
        print("Bravo Kumail, you are a real nigga homie")

#For example, when we are separately printing the individual values of a list or a tupple or anything, and we also want to know which index has what value, we can use the enumerate function, now you dont necessarily have to print the indexes too, but you can if you wanna, however it helps when i want to write something for a specific value at a specific index, like i did for the index 4. 

cars = [45, 74, 21, 38, 98, 23, 12]

for lol, car in enumerate(cars, start= 1):
    print(lol, car)
    if (lol == 3):
        print("Bravo Kumail, you are a real nigga homie")

    else:
        print("Fuck you loser")

#Another thing that we can do with enumerate is that we can start the index from 1, instead of 0. 
