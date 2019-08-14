import random
from random import randint

weapon = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}
request = {'y': 'yes', 'n': 'no', 'sc': 'score'}
player_score = 0
computer_score = 0
player = False
computer = random.choice(list(weapon.keys()))

while player == False:
    player = input("Make A Move (r/s/p):")
    if player == computer:
        print("You chose", player,"and the computer chose", computer,". It's a tie!")
    elif player == "r":
        if computer == "p":
            print("You chose", player,"and the computer chose", computer,". You Lose.")
            computer_score += 1
        else:
            print("You chose", player,"and the computer chose", computer,". You win!")
            player_score += 1
    elif player == "p":
        if computer == "r":
            print("You chose", player,"and the computer chose", computer,". You Lose.")
            computer_score += 1
        else:
            print("You chose", player,"and the computer chose", computer,". You win!")
            player_score += 1
    elif player == "s":
        if computer == "r":
            print("You chose", player,"and the computer chose", computer,". You Lose.")
            computer_score += 1
        else:
            print("You chose", player,"and the computer chose", computer,". You win!")
            player_score += 1
    else: 
        print("Please choose r, p, or s")
        player = False 
        
    computer = random.choice(list(weapon.keys()))
    anothergame = input("Do you want try again? (y/n)(sc for score):")
    if anothergame == "sc":
        print("Player: ", player_score," Computer: ", computer_score)
        anothergame = input("Do you want to try again? (y/n):")
        if anothergame == "y":
            player = False
        elif anothergame == "n": 
            print("thanks bye!")
            break
    elif anothergame == "y":
        player = False
    elif anothergame == "n": 
        print("thanks bye!")