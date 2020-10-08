#Rock, paper, scissors game
from random import randint

#list called options
options = ["ROCK", "PAPER", "SCISSORS"]

#Dictionary that holds messages
message = {
  "tie" : "Yawn it's a tie!",
  "won" : "Yay you won!",
  "lost" : "Aww you lost!"
}

#Function dictates who wins based on user and computers choices
def decide_winner(user_choice, computer_choice):
    print("You selected: %s" % user_choice) 
    print("Computer selected: %s" % computer_choice) 
#Protects against user not entering Rock, Paper, or Scissors
    if user_choice != options[0] and user_choice != options[1] and user_choice != options[2]:
        print("You must choose " + options[0] + ", " + options[1] + ", or " + options[2])
#If user and computer throw same its a tie
    elif user_choice == computer_choice:
        print(message["tie"])
#If user throws Rock and computer throws scissors the user wins
    elif user_choice == options[0] and computer_choice == options[2]:
        print(message["won"])
#If user throws paper and computer throws rock the user wins
    elif user_choice == options[1] and computer_choice == options[0]:
        print(message["won"])
#If user throws scissors and computer throws paper the user wins
    elif user_choice == options[2] and computer_choice == options[1]:
        print(message["won"])
#Every other scenario the computer wins
    else:
        print(message["lost"])

#Function to play game
def play_RPS():
    user_choice = input("Enter Rock, Paper, or Scissors: ")
    user_choice = user_choice.upper()
    computer_choice = options[randint(0, 2)]
    decide_winner(user_choice, computer_choice)

#function that runs the game
play_RPS()