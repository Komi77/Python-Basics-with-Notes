import time
alpha = time.strftime('%H:%M:%S')

a = int(time.strftime('%H'))

timestamp = int(time.strftime('%M'))

timestamp = int(time.strftime('%S'))

# https://docs.python.org/3/library/time.html#time.strftime


if(a >= 1 and a <= 5):
    print("Good Midnight", alpha)

elif(a>5 and a <= 13):
    print("Good Morning", alpha)

elif(a >13 and a<= 19):
    print("Good Afternoon", alpha)

elif(a > 19 and a <= 24):
    print("Good Night", alpha)

else:
    print("You have entered the wrong time dumbass")
