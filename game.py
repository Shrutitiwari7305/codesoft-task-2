import random

def play_game(player_choice):
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    print(f"\nYour choice: {player_choice}")
    print(f"Computer's choice: {computer_choice}")

    if player_choice == computer_choice:
        return "It's a tie!"
    elif (
        (player_choice == "rock" and computer_choice == "scissors") or
        (player_choice == "paper" and computer_choice == "rock") or
        (player_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win!"
    else:
        return "You lose!"

# Get user input for the game
while True:
    user_input = input("Enter your choice (rock, paper, scissors) or 'exit' to end: ").lower()

    if user_input == "exit":
        print("Thanks for playing. Goodbye!")
        break

    if user_input in ["rock", "paper", "scissors"]:
        result = play_game(user_input)
        print(result)
    else:
        print("Invalid choice. Please enter 'rock', 'paper', 'scissors', or 'exit'.")
