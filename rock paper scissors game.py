import tkinter as tk
from tkinter import messagebox
import random
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"
def play_game(player_choice):
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    
    result = determine_winner(player_choice, computer_choice)
    
    messagebox.showinfo("Result", f"Your choice: {player_choice}\nComputer's choice: {computer_choice}\n\n{result}")
    
    play_again = messagebox.askyesno("Play Again?", "Do you want to play again?")
    if not play_again:
        root.destroy()

def main():
    global root
    root = tk.Tk()
    root.title("Rock Paper Scissors Game")
    
    label = tk.Label(root, text="Select your choice:")
    label.pack(pady=10)
    
    rock_button = tk.Button(root, text="Rock", width=10, command=lambda: play_game("rock"))
    rock_button.pack(pady=5)
    
    paper_button = tk.Button(root, text="Paper", width=10, command=lambda: play_game("paper"))
    paper_button.pack(pady=5)
    
    scissors_button = tk.Button(root, text="Scissors", width=10, command=lambda: play_game("scissors"))
    scissors_button.pack(pady=5)
    
    root.mainloop()

if __name__ == "__main__":
    main()

