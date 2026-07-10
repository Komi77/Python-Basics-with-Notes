a = int(input("Enter any number b/w 5 and 9: "))

if a<5 or a>9:
    raise ValueError ("Nigga you can only write values b/w 5 and 9")

#What we did here is basically rhat we said that you can only input numbers b/w 5 and 9, but how to make python know of this situation. Yes we can use if and else, but in this case we want to raise a custom error so that the stupid user knows that he has entered the wrong value. So, we use the keyword raise and raise a custom error all by ourself.

b = ("No", "body", 'is', 'safe', 'from', 'me')
c = input("Copy that mf: ")
if c != b :
    raise ValueError ("Niggaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") 


nigga = "quit"
whigga = "QUIT"
chigga = input("Do you wanna quit: ")

if chigga != nigga and chigga != whigga:
    raise SyntaxError ("Mf are u okay, fuking hell just write it")