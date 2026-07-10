try:
    b = int(input("Enter your number: "))
    c = [6,3, 1, 2, 9]
    print(c[b])

except:
    print("Some fucking dickhead produced an error")

finally:
    print("I will always run mother fucker")


#Whatever we write inside the finally block will always run regardless and error occurs or not, now the main thing is that you might think that if we just wrote print itself, without writing it inside the finally block, it would have worked and be printed anyways. You are right, however finally is necessary when we are wrapping this whole thing inside a function. ANd in a func if you directly write print statement (without indending it), it would not be printed and work, thats why we use finally.

#If we want to do something or execute something of that try gets executed or except, put that shit in finally.



def func1():
    try:
        b = int(input("Enter your number: "))
        c = [6,3, 1, 2, 9]
        print(c[b])
        return True
    except:
            print("Some fucking dickhead produced an error")
            return False, "You dickhead"
    finally:
            print("I will always run mother fucker")


x = func1()
print(x)