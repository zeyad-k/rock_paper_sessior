import tkinter as tk
from tkinter import messagebox
import random

def get_computer_choice():
    choices = ['r', 'p', 's']
    return random.choice(choices)

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie"
    elif (user == 'r' and computer == 's') or (user == 'p' and computer == 'r') or (user == 's' and computer == 'p'):
        return "Player wins -You won-"
    else:
        return "Computer wins -You lost-"

def on_button_click(choice):
    computer = get_computer_choice()
    result = determine_winner(choice, computer)
    messagebox.showinfo("Result", f"Player choice is: {choice}\nComputer choice is: {computer}\n{result}")

# Create the main window
window = tk.Tk()
window.title("Rock-Paper-Scissors Game")

# Create buttons for user choices with improved appearance
button_font = ('Helvetica', 16)
button_width = 10
button_height = 2

# Red Rock Button
rock_button = tk.Button(window, text="Rock", command=lambda: on_button_click('r'), font=button_font, width=button_width, height=button_height, bg='red')

# Blue Paper Button
paper_button = tk.Button(window, text="Paper", command=lambda: on_button_click('p'), font=button_font, width=button_width, height=button_height, bg='blue')

# Green Scissors Button
scissors_button = tk.Button(window, text="Scissors", command=lambda: on_button_click('s'), font=button_font, width=button_width, height=button_height, bg='green')

# Place buttons on the window
rock_button.pack(pady=10)
paper_button.pack(pady=10)
scissors_button.pack(pady=10)

# Start the GUI event loop
window.mainloop()
