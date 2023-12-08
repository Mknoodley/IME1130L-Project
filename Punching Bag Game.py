# This program uses an RNG and functions to simulate a punching bag video game. It is intended to entertain the user
# The user inputs the Punching bag health, how many rounds they will fight for, and inputs if they want to keep fighting after every round. 
# The output consists of telling the player how much damage they've dealt, how much health the punching bag has left, and how many rounds they have left.
import random 

Player_damage = [0, 3, 3, 3, 5, 5, 5, 5, 5, 5, 10, 10, 10]
def Player_attacks():
    return random.choice(Player_damage)

print("Punching Bag: 'How Much Health Should I Have?\nLow = 50 Health\nMedium = 75 Health\nHigh = 100 Health\nIn order to beat me, you must get my health to be exactly 0 by\nthe last round or else you lose.")
Difficulty = input("Low, Medium, or High : ")


Punching_Bag_Health = 1

while Punching_Bag_Health == 1:
    if Difficulty == ("Low") or Difficulty == ("low"):
        Punching_Bag_Health = 50
    elif Difficulty == ("Medium") or Difficulty == ("medium"):
        Punching_Bag_Health = 75
    elif Difficulty == ("High") or Difficulty == ("high"):
        Punching_Bag_Health = 100



Rounds = int(input("How many Rounds will you go for? : "))


for i in range(Rounds):
    Choice = input("Start Round or Quit? Y/N ")
    if Choice == ("Y") or Choice == ("y"):
        if Punching_Bag_Health <= 0:
            print("You Win!")
            break
        elif Player_attacks() == 0:
            print("OOPS! You missed")
        elif Player_attacks() == 3:
            Punching_Bag_Health = Punching_Bag_Health - 3
            print("------- 3 Damge -------")
            print("Punching bag: 'What was that? That was a puny attack you baby!! Do Better!!'")
        elif Player_attacks() == 5:
            Punching_Bag_Health = Punching_Bag_Health - 5
            print("------- 5 Damge -------")
            print("Punching bag: 'That was a good one'!")
        else:
            Punching_Bag_Health = Punching_Bag_Health - 10
            print("------- 10 Damge -------")
            print("Punching bag: 'That was a Great one'!")
    if Choice == ("N") or Choice == ("n"):
        print("Thank you for playing!")
        break

    Rounds_left = (Rounds - i) - 1
    print(str(Rounds_left) + " Rounds Left!")
    print("I have " + str(Punching_Bag_Health) + " Health left")
    if Punching_Bag_Health <= 0:
        print("The bag was destroyed. You went overboard! You lose!")
        break
    if Punching_Bag_Health == 0:
        print("You beat me !")
    if Rounds == i + 1:
        if Punching_Bag_Health > 0:
            print("I win! You Lose!")
            break
        else:
            print("You win!")
            break
    else:
        continue



