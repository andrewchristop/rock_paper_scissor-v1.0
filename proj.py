#Program created by Christopher Andrew from scratch (13/02/2021)
#Version 1.0
#This is an initial release of the source code
#This code is open source, feel free to use my work, don't forget to add proper credits
#Enjoy!
import random
outcomes = ["rock", "paper", "scissor"]
#suggested_inputs = ["rock" , "paper", "scissor"]
user_input = input("Please make a move: ")
comp_move = random.choice(outcomes)

if user_input in outcomes:
    if comp_move == "rock" and user_input == "scissor":
        print("Computer picks: "+ comp_move)
        print("You lose")
    elif comp_move == "paper" and user_input == "rock":
        print("Computer picks: "+ comp_move)
        print("You lose")
    elif comp_move == "scissor" and user_input == "paper":
        print("Computer picks: "+ comp_move)
        print("You lose")
    elif comp_move == user_input:
        print("Computer picks: "+ comp_move)
        print("It's a draw!")
    else:
        print("Computer picks: "+ comp_move)
        print("You win")
else:
    print("Please enter a valid move")
    


