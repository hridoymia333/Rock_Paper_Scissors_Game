import random


def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])


def get_user_choice():
    while True:
        choice = input("Enter rock, paper or scissors: ").lower()
        if choice in ["rock", "paper", "scissors"]:
            return choice
        print("Invalid input, Try again!")


def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or \
        (user == "paper" and computer == "rock") or\
            (user == "scissors" and computer == "paper"):
        return "You Win!"
    else:
        return "Computer Win!"


def play_game():
    print("Welcome to rock, paper, scissors game")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    print(result)


play_game()
