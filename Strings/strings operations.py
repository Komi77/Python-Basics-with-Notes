print("Hey, I am \"Kumail\"")

yesterday = '''
I woke up
I ate breakfast
I chilled
I went to sleep
'''
print(yesterday)
# we use '''  ''' to make multiline strings

name = "Komi"
print(name[0])
print(name[1])
print(name[2])
print(name[3])
#the first letter of the name komi which is K has index number of 0
#Length of a string is different from index because index starts from 0 and len starts from 1. So index of "Komi" will be 0,1,2,3 but its length will be 4


for character in yesterday:
    print(character)
#we can use for loop to count the index numbers of the characters in a string without having to count them manually 

myname = "KumailRaza"
print(len(myname))
#we can find out the length of a string by using the len() function

print(myname[0:6])
#for e.g if i want only the kumail part of my name then in print i can specify the starting index of the character that i want (remember that the character at this index will be included in the result), then if i want the last character which in this case is "L", we write the index of the character next to it because this character will not be included, means if "L" is at the index 5, we cannot write 5 after the colon because it wont be included.

fruit = "mango"
print(fruit[0:-3])
#here only ma will be printed because the length of mango is 5, its starts with 0 index and finishes at -3 index which means 5-3 index which is 2, and we know the character at the index 2 wont be included, so the result is just ma

print(fruit[-3:5])
#similarly here now the python will calculate the string from the index 5-3 which is 2, so n will be included till the last index which is 5

print(fruit[-3:-1])

nm = "Harry"
print(len(nm))
print(nm[-4:-2])

a = "Football"
print(a.upper())
#strings are immutable so when we make them capitalized by the function .upper(), it doesnt edit the o.g. string instead it makes a new string in capitl letters
print(a.lower())

b = "Football!!!!!!!!!!!"
print(b.rstrip("!"))
#this function will remove any letter or number or anything which repeating or trailing at the end.
#NOTE: It doesnt remove the repeating characters at the start

c = "Footballuuuuuuuuuu"
print(c.rstrip("u"))

d = "!!!!!!!!!!!!!Football!!!!!!"
print(d.rstrip("!"))

e = "Debruyne"
print(e.replace("Debruyne", "Kroos"))

f = "Debruyne is a good player, Debruyne brings out his magic on the field"
print(f.replace("Debruyne", "Kroos"))
#means it will replace the highlighted word at all instances with another one

g = "Ronaldo Messi Neymar Mbappe Halaand"
print(g.split())
# means it will turn this string into a list on the basis of the spaces between them like there is a space b/w Ronaldo and messi so they will be two separate components of the list.

blog = "introducTion TO AsTronomy"
print(blog.capitalize())
#Means it will capitalize the first letter of the first word of string but make all the rest letters lower case.

console = "Welcome to the console"
print(len(console))
print(console.center(50))
print(len(console.center(50)))
#means that the length of the string itself is 22, and we set the value of center at 50 which means that it will leave the space from start by 50-22 which is 23. 

nature = "Kumail is a good boy. Kumail sleeps early and Kumail wakes up early"
print(nature.count("Kumail"))
#means we can count how many times a word came in a string like kumail cames 3 times.

disaster = "Fire!!!!!!!!"
print(disaster.endswith("!"))
#means it will tell that does a string end with a specific character or not.

console2 = "Welcome to the console"
print(console2.endswith("to", 4, 10))
#means that does the string end with the specific characters when we splice it such that it starts from the index 4 and ends at 10 which means that 10 wont be included. So, in that case does the string end with the the characters "to", the ans is true.

man = "He's a good man. He is lovely and he is not a kneegrow"
print(man.find("is"))
#means that python will find the highlighted word, more like it will find its index. Now one think to notice here is that python can't understand short forms so it will not interpret He's as He is.
print(man.find("ishh"))
#python will return -1 because ishh doesnt exist in the string.



#NOTE:
'''print(man.index("ishh"))'''

#only different b/w index and find is that when something doesn't exist find returns -1, while index returns an error.


console3 = "Welcome to the console"
print(console3.isalnum())
#this func finds out if the elements of the string are A-Z or a-z or 0-9. Any numbers or symbols other than this give false result. And even spaces b/w letters will give false result.

falsetest = "56"
print(falsetest.isalnum())


str1 = "Welcometotheconsole"
print(str1.isalpha())
#it will only return true result if the characters inside the strings are from A-Z or a-z.

str2 = "Welcometotheconsole000"
print(str2.isalpha())

str3 = "WelcOmetotheconSole"
print(str3.islower())

str4 = "WelcOmetotheconSole\n"
print(str4.isprintable)
#means it identifies whether all the characters in the string are real characters not function, in this case \n is an escape function so it will not be counted as a printable character.

laugh = "The joke was so bad"
print(laugh.isspace())
#identifies if there is a space or gap in the string.

mybook = "the jurrasic end of world"
print(mybook.istitle())
#identifies if every first letter of every word in a string is capitalized or not.

print(mybook.startswith("the"))

print(mybook.swapcase())
#turns all capital letters to lower case and vice versa

print(mybook.title())
#turns all the first letter of every word to Upper case