from tkinter import messagebox
import tkinter as tk
from random import choice

# Game Setup:
FONT_NAME = "Comic Sans MS"
COLOR_DARK_GRAY= "#45474B"
COLOR_LIGHT_GRAY= "#686D76"
COLOR_BLUE = "#050C9C"
COLOR_RED = "#C80036"
COLOR_YELLOW = "#FFEEA9"

players = ["X", "O"]
player = choice(players)
board = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
        ]

game_over = False

def next_turn(row, column):
    global player, players
    if game_over:
        return
    if board[row][column]['text'] == '':
        
        if player == players[0]:  # player = X
            board[row][column].config(text=player)
            player = players[1]  # Reset player To ==> O
        else:
            board[row][column].config(text=player, foreground=COLOR_RED)
            player = players[0]
        title.config(text=f"Player {player}")
    else:
        messagebox.showerror("Error", "This button is already clicked")

    check_winner()

def check_winner():
    global game_over
    # Check the winner Horizontally:
    for row in range(3):
        if (board[row][0]['text'] == board[row][1]['text'] == board[row][2]['text']
            and board[row][0]['text'] != ""):
            title.config(text=f"Player {board[row][0]['text']} Is Winner.",
                        fg=COLOR_YELLOW)
            
            for column in range(3):
                board[row][column].config(foreground=COLOR_YELLOW, 
                                            background=COLOR_LIGHT_GRAY)
                
            game_over = True
            return

    
    # Check the winner Vertically:
    for column in range(3):
        if (board[0][column]['text'] == board[1][column]['text'] == board[2][column]['text']
            and board[0][column]['text'] != ""):
            for row in range(3):
                board[row][column].config(foreground=COLOR_YELLOW, 
                                            background=COLOR_LIGHT_GRAY)
                title.config(text=f"Player {board[0][column]['text']} Is Winner",
                            foreground=COLOR_YELLOW)
            game_over = True
            return
    
    # Check the winner Diagonally:
    if (board[0][0]['text'] == board[1][1]['text'] == board[2][2]['text']
        and board[0][0]['text'] != ""):
        for i in range(3):
            board[i][i].config(foreground=COLOR_YELLOW, 
                                background=COLOR_LIGHT_GRAY)
            title.config(text=f"Player {board[0][0]['text']} Is Winner",
                        foreground=COLOR_YELLOW)
        game_over = True
        return
        
    # Check the winner anti Diagonally:
    if (board[0][2]['text'] == board[1][1]['text'] == board[2][0]['text'] 
        and board[0][2]['text'] != ""):
        board[0][2].config(foreground=COLOR_YELLOW, 
                            background=COLOR_LIGHT_GRAY)
        board[1][1].config(foreground=COLOR_YELLOW, 
                            background=COLOR_LIGHT_GRAY)
        board[2][0].config(foreground=COLOR_YELLOW, 
                            background=COLOR_LIGHT_GRAY)
        
        title.config(text=f"Player {board[0][2]['text']} Is Winner",
                    foreground=COLOR_YELLOW)
        game_over = True
        return
    
def play_again():
    global game_over, player, board
    game_over = False
    player = choice(players)
    title.config(text=f"Player {player}")
    for row in range(3):
        for column in range(3):
            board[row][column]['text'] = ''
            board[row][column].config(foreground=COLOR_BLUE, 
                                        background=COLOR_DARK_GRAY)
    title.config(text=f"Player {player}")
    
# Game Window
window = tk.Tk()
window.title("Tic Tac Toe Game")
window.resizable(False, False)

# Create Frame:
frame = tk.Frame(window)
frame.pack()

# Create Title:
title = tk.Label(frame, text=f"Player {player}", 
                font=(FONT_NAME, 20),
                foreground='white', 
                background=COLOR_DARK_GRAY
                )

title.grid(row=0, column=0, columnspan=3, sticky="we")

# Create Buttons:
for row in range(3):
    for column in range(3):
        # print(row, column)
        board[row][column] = tk.Button(frame, width=5, height=1,
                                        font=(FONT_NAME, 50, "bold"),
                                        foreground=COLOR_BLUE, 
                                        background=COLOR_DARK_GRAY,
                                        command=lambda row=row, column=column: next_turn(row, column))
        board[row][column].grid(row=row + 1, column=column)


rest_button = tk.Button(frame, text="Play Again", 
                        font=(FONT_NAME, 20),
                        foreground='white', 
                        background=COLOR_DARK_GRAY,
                        command=play_again
                        )
rest_button.grid(row=4, column=0, columnspan=3, sticky='ew')

# Set Window In Center Position:
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop()