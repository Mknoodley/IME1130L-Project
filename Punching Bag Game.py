import random 

print("What difficulty level do you choose?")
Difficulty = input("Easy, Medium, or Hard : ")

Punching_Bag_Health_list = [50, 75, 100]

Punching_Bag_Health = 0

while Punching_Bag_Health == 0:
    if Difficulty == "Easy" or Difficulty == "easy":
        Punching_Bag_Health = 50
    elif Difficulty == "Medium":
        Punching_Bag_Health = 75
    elif Difficulty == "Hard":
        Punching_Bag_Health = 100
    

Player_Health = [65]

Bot_damage = [0, 7, 9, 13]

Player_damage = [0, 3, 3, 5, 5, 5, 10]

Rounds = int(input("How many Rounds will you go for? :"))

def Player_attacks():
    return random.choice(Player_damage)

def Bot_attacks():
    return random.choice(Bot_damage)







for i in range(Rounds):
        if Player_attacks() == 0:
            print("OOPS! You missed")
        elif Player_attacks() == 3:
            Punching_Bag_Health = Punching_Bag_Health - 3
            print("-3")
            print("Bot: That was a puny attack!!")
        elif Player_attacks() == 5:
            Punching_Bag_Health = Punching_Bag_Health - 5
            print("Bot: You")
        elif Player_attacks() == 10:
            Punching_Bag_Health = Punching_Bag_Health - 10
            print("OOPS! You missed")
        Rounds_left = Rounds - i
        print(f"{Rounds_left} Rounds Left!")


# This program uses an RNG and functions to simulate a punching bag video game. It is intended to entertain the user
# The user inputs the Punching bag health, how many rounds they will fight for, and inputs if they want to keep fighting after every round. 
# The output consists of telling the player how much damage they've dealt, how much health the punching bag has left, and how many rounds they have left.
import random 

print("Punching Bag: 'How Much Health Should I Have?'")
Difficulty = input("Low, Medium, or High : ")


Punching_Bag_Health = 1

while Punching_Bag_Health == 1:
    if Difficulty == ("Low"):
        Punching_Bag_Health = 50
    elif Difficulty == ("Medium"):
        Punching_Bag_Health = 75
    elif Difficulty == ("High"):
        Punching_Bag_Health = 100
    elif Difficulty == ("low"):
        Punching_Bag_Health = 50
    elif Difficulty == ("medium"):
        Punching_Bag_Health = 75
    elif Difficulty == ("high"):
        Punching_Bag_Health = 100

    
    



Player_damage = [0, 3, 3, 3, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10]

Rounds = int(input("How many Rounds will you go for? :"))

def Player_attacks():
    return random.choice(Player_damage)





for i in range(Rounds):
    Choice = input("Start Round or Quit? Y/N ")
    if Choice == ("Y"):
        if Punching_Bag_Health <= 0:
            print("You Win!")
            break
        elif Player_attacks() == 0:
            print("OOPS! You missed")
        elif Player_attacks() == 3:
            Punching_Bag_Health = Punching_Bag_Health - 3
            print('\033[91m' + "------- 3 Damge -------" + '\033[0m')
            print("Punching bag: 'What was that? That was a puny attack you baby!! Do Better!!'")
        elif Player_attacks() == 5:
            Punching_Bag_Health = Punching_Bag_Health - 5
            print('\033[91m' + "------- 5 Damge -------" + '\033[0m')
            print("Punching bag: 'That was a good one'!")
        else:
            Punching_Bag_Health = Punching_Bag_Health - 10
            print('\033[91m' + "------- 10 Damge -------" + '\033[0m')
            print("Punching bag: 'That was a Great one'!")
    elif Choice == ("y"):
        if Punching_Bag_Health <= 0:
            print("You have Bested Me! Good Game.")
            break
        elif Player_attacks() == 0:
            print("OOPS! You missed")
        elif Player_attacks() == 3:
            Punching_Bag_Health = Punching_Bag_Health - 3
            print('\033[91m' + "------- 3 Damge -------" + '\033[0m')
            print("Punching bag: 'What was that? That was a puny attack you baby!! Do Better!!'")
        elif Player_attacks() == 5:
            Punching_Bag_Health = Punching_Bag_Health - 5
            print('\033[91m' + "------- 5 Damge -------" + '\033[0m')
            print("Punching bag: 'That was a good one'!")
        else:
            Punching_Bag_Health = Punching_Bag_Health - 10
            print('\033[91m' + "------- 10 Damge -------" + '\033[0m')
            print("Punching bag: 'That was a Great one'!")
    else:
        break
    Rounds_left = (Rounds - i) - 1
    print(str(Rounds_left) + " Rounds Left!")
    print("I have " + str(Punching_Bag_Health) + " Health left")
    if Rounds == i + 1:
        if Punching_Bag_Health > 0:
            print("I win! You Lose!")
            break
        else:
            print("You win!")
            break
    else:
        continue
    
    if Punching_Bag_Health <= 0:
        print("You beat me !")
        break
    else:
        continue
