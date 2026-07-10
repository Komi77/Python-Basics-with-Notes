try:

    a = int(input("Enter the number: "))
    print(f"Multiplication table of {a} is: ")

    for i in range(1, 11):
        print(f"{a} X {i} = {a * i}")
except Exception as e:
    print("The value entered is not correct", e)


print("Some lines of code")
print("End of program")


#What happened here was that when i entered a wrong value in the input which means a value which was not an integer, python threw an error at me and the program stopped working and the lines of code after the for loop also werent printed, But i dont want that i want python to continue writing my code even if the for loop is wrong and there is an error. for that we use try and except method, by using it we can bascially throw and sort of print the error that we are facing and the rest of the program goes on.




try:
    b = int(input("Enter your number: "))
    c = [6,3]
    print(c[b])

except ValueError:
    print("Number entered is not an integer")


except IndexError:
    print("Index error")


#Okay first lets understand this code, we have b which takes input then c which is a tupple with just two values in it, now the print statement that we gave is a bit complex, what it basically says is print c of the index b, like we write print(a[2]), means print the value of a at the index 2, now in this program we are saying that the index is whatever the value of b is, and that can create alot of errors, most prominently two errors valueerror and indexerror which can be handled and printed using try and except. If the user gives the value of b which isnt an integer, then we will throw the valueerror because his value is incorrect, but if the user enters an integer, however the integer is a big number like 4 or 7 or anything bigger than 1, we will throw index error, because we cant print(c[4]) because c is a tupple with just two values and max index of 1. But yeah thats is how we can sort of throw different error based on the things the user gets wrong.