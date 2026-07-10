import random

options = ['Rock', 'Paper', 'Scissor']



    
while True:
    user = input("Enter either Rock, Paper or Scissor: ")
    
    
    if (user.lower() == "scissor" or user.lower() == "paper" or user.lower() == "rock"):
                print(f"The user chose {user}")

    else:
                print("The entered value is wrong")


    
    good = random.choice(options)
    print(f"The computer chose {good}")



    user.lower == user.capitalize


    if (good == user.capitalize()):
        print(f"Its a tie because the user chose {user.capitalize()}and the comp chose {good}")

    elif (good == 'Rock' and user.capitalize() == 'Scissor') or (good == 'Paper' and user.capitalize() == 'Rock') or (good == 'Scissor' and user.capitalize() == 'Paper'):

        print(f"The flipping comp wins because it chose {good} and nigga the user chose {user}")
    elif ( user.capitalize() == 'Rock' and good == 'Scissor') or ( user.capitalize() == 'Paper' and good == 'Rock') or ( user.capitalize() == 'Scissor' and good == 'Paper'):
        print(f"Nigga you win because you chose {user} and the dumb comp chose {good}")
    else:
        print("You must have typed the wrong value")


    playagain = input("Do you wanna play again 'Yes' or 'No': ")

    if (playagain.lower() != "yes"):
        print("The game is over chigga")
        break
