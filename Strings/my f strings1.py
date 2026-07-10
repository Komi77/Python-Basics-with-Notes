name = "Kumail"
country = "Pakistan"
letter = f"Hey my name is {name}, and I am from {country}"
print(letter.format(name, country))


club = input("Enter your answer: ")
position = input("Enter your answer: ")

football = f"I support {club} and I play as a {position}"
print(football.format(club, position))




price = 45.099999999999999999
apple = f"Buy these apples for just {price:.2f}"
print(apple.format(price))

#By writing the variable name then putting a semi colon and then writing .2f, we can round of numbers to two decimal places if we write 3f, it will round off to 3 decimal places.

pi = 3.14159
lol = f"The rounded off value of pi to three decimal places is {pi:.3f}"
print(lol.format(pi))


tri = f"the value of 32 and 5 is {32 * 5}"
print(tri)

letter1 = f"Hey my name is {{name}}, and I am from {{country}}"
print(letter1)

#If a I want to literally print {name} and {country}, I can enclose them in a set of more curly brackets.