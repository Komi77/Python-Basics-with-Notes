a = int(input("Enter Your Number: "))

if(a < 0):
    print("Your number is negative")

elif(a>0):
    if(a <= 10):
        print("Your number is b/w 1-10")

    elif(a>10 and a <= 20):
        print("Your num is b/w 11-20")

    else:
        print("Your number is greater than 20")

else:
    print("Your number is zero")


time = int(input("Enter the time: "))

if(time > 20 and time <= 4):
    print("Good Night Sir")

elif(time > 4 and time <= 13):
    print("Good Morning Sir")

elif(time > 13 and time <= 20):
    print("Good Afternoon Sir")

else:
    print("You have entered the wrong time dumbass")
