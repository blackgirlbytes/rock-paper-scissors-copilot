# write a rock paper scissors game
# import the random module
import random

# define main function that handles all the logic
def main():
    # define a list of possible choices
    choices = ["rock", "paper", "scissors"]
    # define a variable that holds the user's choice
    user_choice = input("Enter your choice: ")
    # define a variable that holds the computer's choice
    computer_choice = random.choice(choices)
    # print the user's choice
    print("You chose", user_choice)
    # print the computer's choice
    print("The computer chose", computer_choice)
    # check if the user's choice is rock
    if user_choice == "rock":
        # check if the computer's choice is rock
        if computer_choice == "rock":
            # print a tie message
            print("It's a tie!")
        # check if the computer's choice is paper
        elif computer_choice == "paper":
            # print a lose message
            print("You lose!")
        # check if the computer's choice is scissors
        elif computer_choice == "scissors":
            # print a win message
            print("You win!")
    # check if the user's choice is paper
    elif user_choice == "paper":
        # check if the computer's choice is rock
        if computer_choice == "rock":
            # print a win message
            print("You win!")
        # check if the computer's choice is paper
        elif computer_choice == "paper":
            # print a tie message
            print("It's a tie!")
        # check if the computer's choice is scissors
        elif computer_choice == "scissors":
            # print a lose message
            print("You lose!")
    # check if the user's choice is scissors
    elif user_choice == "scissors":
        # check if the computer's choice is rock
        if computer_choice == "rock":
            # print a lose message
            print("You lose!")
        # check if the computer's choice is paper
        elif computer_choice == "paper":
            # print a win message
            print("You win!")
        # check if the computer's choice is scissors
        elif computer_choice == "scissors":
            # print a tie message
            print("It's a tie!")
    # check if the user's choice is not valid
    else:
        # print an error message
        print("Invalid choice!")

# call the main function
