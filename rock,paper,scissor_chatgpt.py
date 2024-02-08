import random

def get_user_choice():
    """Get the user's choice."""
    while True:
        user = input("Choose your move: 'r' for Rock, 'p' for Paper, 's' for Scissors: ")
        if user in ['r', 'p', 's']:
            return user
        else:
            print("Invalid choice. Please try again.")

def get_computer_choice():
    """Get the computer's choice."""
    choices = ['r', 'p', 's']
    return random.choice(choices)

def determine_winner(user, computer):
    """Determine the winner."""
    if user == computer:
        return "It's a tie!"
    elif (user == 'r' and computer == 's') or (user == 'p' and computer == 'r') or (user == 's' and computer == 'p'):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    """Play the game."""
    while True:
        user = get_user_choice()
        computer = get_computer_choice()
        print(f"Player choice is: {user}")
        print(f"Computer choice is: {computer}")
        print(determine_winner(user, computer))
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() != 'y':
            break

play_game()