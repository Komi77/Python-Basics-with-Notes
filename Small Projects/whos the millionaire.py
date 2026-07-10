print("Welcome to KBC, You have to choose the correct option from four different options.")
print("PRIZE POT:\n$1,000,000\n$500,000\n$250,000\n$100,000\n$0")
print("Your current balance is $1,000,000")

qs1 = ["Messi", "Kaka", "Pele", "Ronaldo"]
print("Your first question is...")
print("Which football player is known as Mr. UCL?\n", qs1)

ans1 = input("Enter your answer: ")

if(ans1 == qs1[3]):
    print("You are correct")
    print("Your New balance is $1,000,000")

else:
    print("You are wrong")
    print("Your New balance is $500,000")

qs2 = ("Jinnah", "Ayub Khan", "Liaqut Khan", "Yahya Khan")
print("Your second question is...")
print("Who was the first president of Pakistan?\n", qs2)

ans2 = input("Enter your answer: ")

if(ans2 == qs2[2]):
    print("You are right!")

    if (ans1 == qs1[3]):
        print("Your new balance is $1,000,000")

    elif(ans1 != qs1[3]):
        print("Your New Balance is $500.000")


elif(ans2 != qs2[2]):
    print("You are wrong")
    if (ans1 == qs1[3]):
        print("Your new balance is $500,000")
    elif(ans1 != qs1[3]):
        print("Your New Balance is $250.000")


qs3 = ("Jupiter", "Mercury", "Venus", "Mars")
print("Your third question is...")
print("Which planet is known as the gas giant\n", qs3)

ans3 = input("Enter Your answer: ")


if(ans3 == qs3[0]):
    print("You are right!")

    if (ans2 == qs2[2]):
        if (ans1 == qs1[3]):
            print("Your new balance is $1,000,000")

        elif(ans1 != qs1[3]):
            print("Your New Balance is $500.000")



    elif(ans2 != qs2[2]):

        if (ans1 == qs1[3]):
            print("Your new balance is $500,000")

        elif(ans1 != qs1[3]):
            print("Your New Balance is $250.000") 

elif(ans3 != qs3[0]):
    print("You are wrong")
    if (ans2 == qs2[2]):
    
        if (ans1 == qs1[3]):
            print("Your new balance is $500,000")

        elif(ans1 != qs1[3]):
            print("Your New Balance is $250.000")
    
    
    elif(ans2 != qs2[2]):
      
        if (ans1 == qs1[3]):
            print("Your new balance is $250,000")

        elif(ans1 != qs1[3]):
            print("Your New Balance is $100.000")


    


qs4 = ("Game of Thrones", "Breaking Bad", "Dexter", "Sopranos")
print("Your fourth question is...")
print("Which is the highest rated T.V. Show\n", qs4)

ans4 = input("Enter Your answer: ")


if(ans4 == qs4[1]):
    print("You are god damn right!")

    if(ans3 == qs3[0]):
    

        if (ans2 == qs2[2]):
            if (ans1 == qs1[3]):
                print("Your new balance is $1,000,000")

            elif(ans1 != qs1[3]):
                print("Your New Balance is $500,000")



        elif(ans2 != qs2[2]):

            if (ans1 == qs1[3]):
                print("Your new balance is $500,000")

            elif(ans1 != qs1[3]):
                print("Your New Balance is $250,000") 



    elif(ans3 != qs3[0]):
        
        if (ans2 == qs2[2]):
    
            if (ans1 == qs1[3]):
                print("Your new balance is $500,000")

            elif(ans1 != qs1[3]):
                print("Your New Balance is $250,000")
    
    
        elif(ans2 != qs2[2]):
      
            if (ans1 == qs1[3]):
                print("Your new balance is $250,000")

            elif(ans1 != qs1[3]):
                print("Your New Balance is $100,000")




elif(ans4 != qs4[1]):
    print("You are wrong")

    if(ans3 == qs3[0]):


        if (ans2 == qs2[2]):
            if (ans1 == qs1[3]):
                print("Your new balance is $500,000")

            elif(ans1 != qs1[3]):
                print("Your New Balance is $250,000")



        elif(ans2 != qs2[2]):

            if (ans1 == qs1[3]):
                print("Your new balance is $250,000")

            elif(ans1 != qs1[3]):
                print("Your New Balance is $100,000") 



    elif(ans3 != qs3[0]):
        
        if (ans2 == qs2[2]):
    
            if (ans1 == qs1[3]):
                print("Your new balance is $250,000")

            elif(ans1 != qs1[3]):
                print("Your New Balance is $100.000")
    
    
        elif(ans2 != qs2[2]):
      
            if (ans1 == qs1[3]):
                print("Your new balance is $100,000")
 
            elif(ans1 != qs1[3]):
                print("Your New Balance is $0")


print("End of the game")






































# qs5 = ("Yellow Fever", "Malaria", "Polio", "Covid")
# print("Your fifth question is...")
# print("Which disease has been cured worldwide but is still abundant in Pakistan?\n", qs5)

# ans5 = input("Enter Your answer: ")

# qs6 = ("UV Rays", "CMB", "Light Rays", "Radio Waves")

# print("Your sixth question is...")
# print("The first rays after the big bang are called...?\n", qs6)

# ans6 = input("Enter Your answer: ")








# if(ans1 == qs1[3]):
#     print("You are correct")
#     print("Your New balance is $1,000,000")

#     if(ans2 == qs1[3]):
#         print("You are correct")
#         print("Your New balance is $1,000,000")

#     else:
#         print("You are wrong")
#         print("Your New balance is $500,000")

#         if(ans1 == qs1[3]):
#             print("You are correct")
#             print("Your New balance is $1,000,000")

#         else:
#             print("You are wrong")
#             print("Your New balance is $500,000")

# else:
#     print("You are wrong")
#     print("Your New balance is $500,000")
